from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from facebookgroupbutton.models import FacebookGroupButton
from django.utils.translation import ugettext as _

class FacebookGroupButtonPlugin(CMSPluginBase):
    model = FacebookGroupButton # Model where data about this plugin is saved
    name = _("Facebook Group Button") # Name of the plugin
    render_template = "facebookgroupbutton/plugin.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'group':instance.group})
        return context

plugin_pool.register_plugin(FacebookGroupButtonPlugin) # register the plugin
