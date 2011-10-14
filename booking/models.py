from django.db import models
import datetime
from django.contrib.auth.models import User

class Spec(models.Model):
  name = models.CharField(max_length=200)
  def __unicode__(self):
    return self.name
  class Meta:
    verbose_name = 'Specification'
    verbose_name_plural = 'Specifications'

class Booking(models.Model):
  user = models.ForeignKey(User)
  approved = models.BooleanField()
  start_date = models.DateTimeField('start date')
  end_date = models.DateTimeField('end date')
  rejection_reason = models.CharField(max_length=200)
  kits = models.ManyToManyField('Kit')
  def __unicode__(self):
    return unicode(self.user)

class Kit(models.Model):
  name = models.CharField(max_length=200)
  amount = models.IntegerField()
  specs = models.ManyToManyField(Spec, blank=True)
  bookings = models.ManyToManyField(Booking, editable=False, null=True)
  def __unicode__(self):
    return self.name
  class Meta:
    verbose_name = 'Kit'
    verbose_name_plural = 'Kit'
  
# Create your models here.
