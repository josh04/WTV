from django.db import models
from sortable.models import Sortable
import datetime

class Exec(Sortable):
  year = models.PositiveIntegerField()
  name = models.CharField(max_length=200)
  role = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  photo = models.FileField(upload_to='exec', blank=True)
  def __unicode__(self):
    return self.role + ' ' + str(self.year)
  def current_exec(self):
    return self.year == datetime.date.today().year
  current_exec.short_description = 'Current exec?'

