from django import forms
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import permission_required
from django.template import RequestContext
from zinnia.admin.widgets import MPTTFilteredSelectMultiple, MPTTModelMultipleChoiceField
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response
from zinnia.models import Entry, Category
from zinnia.managers import DRAFT, PUBLISHED
from cms.plugin_rendering import render_placeholder
from django.http import Http404, HttpResponseRedirect
from textvid.models import TextVidModel
from cms.plugins.text.models import Text as TextModel
from textvid.cms_plugins import TextVidPlugin
from cms.plugins.text.cms_plugins import TextPlugin
import cms.api

class WTVAddEntryForm(forms.ModelForm):
  tags = forms.BooleanField(required=False, label=_('Front page ticker'))

  categories = MPTTModelMultipleChoiceField(
    Category.objects.all(), required=False, label=_('Categories'),
    widget=MPTTFilteredSelectMultiple(_('categories'), False, attrs={'rows': '10'}))

  def __init__(self, *args, **kwargs):
      super(WTVAddEntryForm, self).__init__(*args, **kwargs)

  class Meta:
    """EntryAdminForm's Meta"""
    model = Entry
    fields = ('title', 'tags', 'categories')

class WTVAddShoutboxForm(forms.ModelForm):
  class Meta:
    """EntryAdminForm's Meta"""
    model = Entry
    fields = ('title',)


@permission_required('zinnia.add_entry')
def wtv_add_entry(request):
  """View for quickly post an Entry"""
  if request.POST:
    form = WTVAddEntryForm(request.POST)
    if form.is_valid():
      entry = form.save(commit=False)
      entry.status = DRAFT
      entry.slug = slugify(entry.title)
      if entry.tags == "True":
        entry.tags = 'video'
      else:
        entry.tags = ''
      entry.save()
      form.save_m2m()
      entry.sites.add(Site.objects.get_current())
      entry.authors.add(request.user)
      plugin = cms.api.add_plugin(entry.content_placeholder, TextVidPlugin, 'en-gb')
      return HttpResponseRedirect(reverse('wtvforms.views.wtv_add_entry_content', args=(plugin.id,)))
  else:
    form = WTVAddEntryForm() 

  return render_to_response('wtvforms/wtv_add_entry.html', {'form': form }, context_instance=RequestContext(request) )

@permission_required('zinnia.add_entry')
def wtv_add_entry_content(request, plugin_id, message=''):
#  plugin = get_object_or_404(CMSPlugin, pk=plugin_id)

  try:
    plugin = TextVidModel.objects.get(pk=plugin_id)
  except TextVidModel.DoesNotExist:
    raise Http404
  textVid = TextVidPlugin()
  formClass = textVid.get_form(request, obj=plugin)
  if request.POST:
    form = formClass(request.POST, instance=plugin)
    if form.is_valid():
      plugin = form.save()
      entry = Entry.objects.get(content_placeholder__id=plugin.placeholder_id)
      entry.status = PUBLISHED
      context = RequestContext(request)
      entry.content = render_placeholder(entry.content_placeholder, context)
      entry.save()
      message = _('The video has been added to the site.')
    else:
      message = _('The video has not been added to the site.')
  else :
    form = formClass(instance=plugin)
  return render_to_response('wtvforms/wtv_add_entry_content.html', {'form': form, 'message': message }, context_instance=RequestContext(request) )

@permission_required('zinnia.add_entry')
def wtv_add_shoutbox(request, mode):
  """View for quickly post an Entry"""
  if request.POST:
    form = WTVAddShoutboxForm(request.POST)
    if form.is_valid():
      entry = form.save(commit=False)
      entry.status = DRAFT
      entry.slug = slugify(entry.title)
      entry.save()
      entry.sites.add(Site.objects.get_current())
      entry.authors.add(request.user)
      if (mode == 7):
        entry.categories.add(7)
      else:
        entry.categories.add(6)
      plugin = cms.api.add_plugin(entry.content_placeholder, TextPlugin, 'en-gb')
      return HttpResponseRedirect(reverse('wtvforms.views.wtv_add_shoutbox_content', args=(plugin.id,)))
  else:
    form = WTVAddShoutboxForm()

  return render_to_response('wtvforms/wtv_add_shoutbox.html', {'form': form }, context_instance=RequestContext(request) )

@permission_required('zinnia.add_entry')
def wtv_add_shoutbox_content(request, plugin_id):
  try:
    plugin = TextModel.objects.get(pk=plugin_id)
  except TextModel.DoesNotExist:
    raise Http404
  text = TextPlugin()
  formClass = text.get_form(request, obj=plugin)
  if request.POST:
    form = formClass(request.POST, instance=plugin)
    if form.is_valid():
      plugin = form.save()
#(TODO) needs a get_object or 404 here. v. important
      entry = Entry.objects.get(content_placeholder__id=plugin.placeholder_id)
      entry.status = PUBLISHED
      context = RequestContext(request)
      entry.content = render_placeholder(entry.content_placeholder, context)
      entry.save()
      return HttpResponseRedirect(reverse('wtvforms.views.wtv_add_shoutbox_content', args=(plugin.id,)))
  else :
    form = formClass(instance=plugin)
  return render_to_response('wtvforms/wtv_add_shoutbox_content.html', {'form': form}, context_instance=RequestContext(request) )


