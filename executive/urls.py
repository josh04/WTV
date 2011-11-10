from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'executive.views.current_exec'),
)
