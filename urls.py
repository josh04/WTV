from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^archive/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    (r'^polls/', include('polls.urls')),
    (r'^booking/', include('booking.urls')),
    url(r'^wtv/', include('wtvforms.urls')),
    (r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
