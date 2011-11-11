from django.conf.urls.defaults import *
from executive.models import Exec

info_dict = {
    'queryset': Exec.objects.all(),
}

urlpatterns = patterns('',
    (r'^edit/$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^view/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
    (r'^edit/(?P<object_id>\d+)/$', 'django.views.generic.create_update.update_object', { 'model':Exec, 'post_save_redirect':'/exec/edit/', 'login_required': True }),
    (r'^$', 'executive.views.current_exec'),
)
