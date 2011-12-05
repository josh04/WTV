from django.db import models
from cms.plugins.text.models import AbstractText

class TextVidModel(AbstractText):
  youtube_id = models.CharField(max_length=12)

