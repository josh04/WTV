from django.db import models
import datetime
from django.contrib.auth.models import User

# class Spec(models.Model):
#   name = models.CharField(max_length=200)
#   def __unicode__(self):
#     return self.name
#   class Meta:
#     verbose_name = 'Specification'
#     verbose_name_plural = 'Specifications'

class Booking(models.Model):
    user = models.ForeignKey(User)

    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')

    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    rejection_reason = models.TextField(default='', blank=True)

    kits = models.ManyToManyField('Kit')

    def clean(self):
        from django.core.exceptions import ValidationError

        # Make sure that rejected bookings aren't approved.
        if self.rejected and self.approved:
            raise ValidationError('A booking cannot be approved and rejected')

        # Make sure that rejection_reason is blank if not rejected
        if self.rejected == False:
            # Clear the rejection reason field.
            self.rejection_reason = ''

        # Make sure that the kit will not already be booked out.
        result = self.kits.objects.filter(
            booking_set__end_date__gte=self.start_date
            ).exclude(
            booking_set__start_date__gte=self.end_date
            )

        if len(result) > 0:
            ValidationError('The following kit was booked out: %s' % result)

        super(Booking, self).clean()

    def __unicode__(self):
        return unicode(self.user)

class KitType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Kit(models.Model):
    type = models.ForeignKey(KitType)
    serial = models.CharField(max_length=50, unique=True)
    in_store = models.BooleanField(default=True)

    def booked_out(self, from_date, to_date):
        '''
        Check to see if the kit is booked out during this period.
        '''

        # Get all of the associated bookings with an end data larger than from and smaller
        # than to.
        result = bookings.objects.filter(
            end_date__gte=from_date
            ).exclude(
            start_date__gte=to_date
            )

        if len(result) > 0:
            return True
        else:
            return False


    def __unicode__(self):
        return self.serial

    class Meta:
        verbose_name = 'Kit'
        verbose_name_plural = 'Kit'

# Create your models here.
