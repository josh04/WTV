from django.db import models
from cms.models import CMSPlugin

class FacebookGroupButton(CMSPlugin):
    group = models.CharField(max_length=200)

    def __unicode__(self):
      return self.group

