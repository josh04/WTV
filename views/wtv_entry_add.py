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


from zinnia.admin.widgets import MPTTFilteredSelectMultiple

from zinnia.admin.widgets import MPTTModelMultipleChoiceField

from django.utils.translation import ugettext_lazy as _

from django.shortcuts import render_to_response

from zinnia.models import Entry, Category
from zinnia.managers import DRAFT, PUBLISHED

from django import forms


class WTVAddEntryForm(forms.ModelForm):
  title = forms.CharField(required=True, max_length=255)
  content = forms.CharField(required=True)
  tags = forms.BooleanField(required=False)

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



@permission_required('zinnia.add_entry')
def view_wtv_entry_add(request):
    """View for quickly post an Entry"""
    if request.POST:
        form = WTVAddEntryForm(request.POST)
        if form.is_valid():
            entry_dict = form.cleaned_data
            status = PUBLISHED
            entry_dict['content'] = linebreaks(entry_dict['content'])
            entry_dict['slug'] = slugify(entry_dict['title'])
            entry_dict['status'] = status
            entry = Entry.objects.create(**entry_dict)
            entry.sites.add(Site.objects.get_current())
            entry.authors.add(request.user)
            return redirect(entry)

        data = {'title': smart_str(request.POST.get('title', '')),
                'content': smart_str(linebreaks(request.POST.get('content', '')))}
        return redirect('%s?%s' % (reverse('add'), urlencode(data)))
    return render_to_response('wtv_add_entry.html', {'form': WTVAddEntryForm() } )


