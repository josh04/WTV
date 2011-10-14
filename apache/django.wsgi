import os, sys
sys.path.append('/home/django')
sys.path.append('/home/django/wtv')
sys.path.append('/usr/local/lib/python2.6/dist-packages/appmedia')
os.environ['DJANGO_SETTINGS_MODULE'] = 'wtv.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
