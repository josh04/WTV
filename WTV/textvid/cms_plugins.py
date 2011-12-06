from cms.plugins.text.utils import plugin_tags_to_user_html
from django.forms.fields import CharField
from cms.plugin_pool import plugin_pool
from textvid.models import TextVidModel
from django.utils.translation import ugettext as _
from cms.plugins.text.cms_plugins import TextPlugin
from urlparse import urlparse,parse_qs
from django.core.exceptions import ValidationError


class TextVidPlugin(TextPlugin):
  model = TextVidModel # Model where data about this plugin is saved
  name = _("WTV Video") # Name of the plugin
  render_template = "textvid/plugin.html" # template to render the plugin with
  change_form_template = "textvid/text_plugin_change_form.html"

  def get_form_class(self, request, plugins):
    """
    Returns a subclass of Form to be used by this plugin
    """
    # We avoid mutating the Form declared above by subclassing
    class TextPluginForm(self.form):
      def clean_youtube_id(self):
        youtube_url = urlparse(self.cleaned_data['youtube_id'])
        params = parse_qs(youtube_url.query)
        try:
          return params['v'][0]
        except KeyError:
          raise ValidationError(u'You did not enter a valid youtube id.')
          

    widget = self.get_editor_widget(request, plugins)
    TextPluginForm.declared_fields["body"] = CharField(widget=widget, required=False)
    TextPluginForm.declared_fields["youtube_id"] = CharField(required=False, label='Youtube URL')
    return TextPluginForm

  def get_form(self, request, obj=None, **kwargs):
    if obj:
      if obj.youtube_id:
        youtube_string = 'http://www.youtube.com/watch?v='
        youtube_string += obj.youtube_id
        obj.youtube_id = youtube_string
    plugins = plugin_pool.get_text_enabled_plugins(self.placeholder, self.page)
    form = self.get_form_class(request, plugins)
    kwargs['form'] = form # override standard form
    return super(TextVidPlugin, self).get_form(request, obj, **kwargs)

  def render(self, context, instance, placeholder):
    context.update({
      'body': plugin_tags_to_user_html(instance.body, context, placeholder),
      'placeholder': placeholder,
      'object': instance,
    })
    return context


  def save_model(self, request, obj, form, change):
    obj.clean_plugins()
    super(TextPlugin, self).save_model(request, obj, form, change)

plugin_pool.register_plugin(TextVidPlugin) # register the plugin

