from django.conf.urls.defaults import *

info_dict = {
}

urlpatterns = patterns('',
   (r'^add/(?P<plugin_id>\d+)/$', 'wtvforms.views.wtv_add_entry_content'), 
   url(r'^add/', 'wtvforms.views.wtv_add_entry'),  
   (r'^shoutbox/(?P<plugin_id>\d+)/$', 'wtvforms.views.wtv_add_shoutbox_content'),
   url(r'^shoutbox/', 'wtvforms.views.wtv_add_shoutbox'),
)
