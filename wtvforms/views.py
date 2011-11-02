from django import forms
from django.utils.html import linebreaks
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
from django.utils.encoding import smart_str
from django.contrib.auth.decorators import permission_required

from django.db.models import ManyToManyRel

from django.contrib.admin.widgets import RelatedFieldWidgetWrapper

from django.template import RequestContext

from zinnia.admin.widgets import MPTTFilteredSelectMultiple

from zinnia.admin.widgets import MPTTModelMultipleChoiceField

from django.utils.translation import ugettext_lazy as _

from django.shortcuts import render_to_response, get_object_or_404

from zinnia.models import Entry, Category
from zinnia.managers import DRAFT, PUBLISHED

from django import forms
from django.http import Http404, HttpResponse, HttpResponseRedirect
from cms.models.fields import PlaceholderField
from cms.forms.widgets import PlaceholderPluginEditorWidget
from textvid.models import TextVidModel
from textvid.cms_plugins import TextVidPlugin

class WTVAddEntryForm(forms.ModelForm):
  tags = forms.BooleanField(required=False, label=_('Front page ticker'))

  categories = MPTTModelMultipleChoiceField(
    Category.objects.all(), required=False, label=_('Categories'),
    widget=MPTTFilteredSelectMultiple(_('categories'), False,
                                      attrs={'rows': '10'}))

  def __init__(self, *args, **kwargs):
      super(WTVAddEntryForm, self).__init__(*args, **kwargs)
      rel = ManyToManyRel(Category, 'id')

  class Meta:
    """EntryAdminForm's Meta"""
    model = Entry
    fields = ('title', 'tags', 'categories')

@permission_required('zinnia.add_entry')
def wtv_add_entry(request):
  """View for quickly post an Entry"""
  if request.POST:
    form = WTVAddEntryForm(request.POST)
    if form.is_valid():
      entry = form.save(commit=False)
      entry.status = DRAFT
      entry.slug = slugify(entry.title)
      if entry.tags == False:
        entry.tags = 'video'
      entry.save()
      entry.sites.add(Site.objects.get_current())
      entry.authors.add(request.user)
      plugin = cms.api.add_plugin(entry.content_placeholder, TextVidPlugin, 'en-gb')
      return HttpResponseRedirect(reverse('wtvforms.views.wtv_add_entry_content', args=(plugin.id,)))
  else:
    form = WTVAddEntryForm() 

  return render_to_response('wtv_add_entry.html', {'form': form }, context_instance=RequestContext(request) )

@permission_required('zinnia.add_entry')
def wtv_add_entry_content(request, plugin_id):
  entry = get_object_or_404(Entry, pk=plugin_id)
  if request.POST:
    form = WTVAddEntryContentForm(request.POST, instance=entry)
    if form.is_valid():
      entry = form.save(commit=False)
      return HttpResponseRedirect(reverse('add_entry_content', args=(entry.id,)))
    
  textPlugin = TextVidPlugin()
  form = textPlugin.get_form(request)

  return render_to_response('wtv_add_entry_content.html', {'form': form }, context_instance=RequestContext(request) )

 
