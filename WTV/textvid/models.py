from django.db import models
from cms.plugins.text.models import AbstractText
from django.core.exceptions import ValidationError

class TextVidModel(AbstractText):
  youtube_id = models.CharField(max_length=12)

def validate_youtube(youtube_id):
  if (len(youtube_id) > 11):
    raise ValidationError(u'You did not enter a valid youtube id.')
