from django.conf.urls.defaults import *
from booking.models import Kit, Booking

info_dict = {
  'queryset': Kit.objects.all(),
}

create_booking = {
  'model': Booking,
  'post_save_redirect': '/booking/',
}



urlpatterns = patterns('',
  (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
  (r'^create/', 'django.views.generic.create_update.create_object', create_booking),
  (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
)
