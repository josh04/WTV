from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ExecApp(CMSApp):
    name = _("Current Executive") # give your app a name, this is required
    urls = ["executive.urls"] # link your app to url configuration(s)

apphook_pool.register(ExecApp) # register your app

