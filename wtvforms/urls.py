from django.conf.urls.defaults import *

info_dict = {
}

urlpatterns = patterns('',
   (r'^(?P<plugin_id>\d+)/$', 'wtvforms.views.wtv_add_entry_content'), 
   url(r'^', 'wtvforms.views.wtv_add_entry'),  
)
