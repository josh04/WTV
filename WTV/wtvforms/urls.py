from django.conf.urls.defaults import *


urlpatterns = patterns('',
   (r'^add-video/(?P<plugin_id>\d+)/$', 'wtvforms.views.wtv_add_entry_content'), 
   url(r'^add-video/', 'wtvforms.views.wtv_add_entry'),  
   (r'^add-shoutbox/(?P<plugin_id>\d+)/$', 'wtvforms.views.wtv_add_shoutbox_content'),
   url(r'^add-shoutbox/', 'wtvforms.views.wtv_add_shoutbox', { 'mode': 7 } ),
   (r'^add-news/(?P<plugin_id>\d+)/$', 'wtvforms.views.wtv_add_shoutbox_content'),
   url(r'^add-news/', 'wtvforms.views.wtv_add_shoutbox', { 'mode': 6 } ),
)
