from django.db import models
from cms.models import CMSPlugin
from cms.plugins.text.models import AbstractText
import datetime

class TextVidModel(AbstractText):
  youtube_id = models.CharField(max_length=12)

