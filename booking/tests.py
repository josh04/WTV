"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from booking.models import KitType, Kit, Booking
from django.contrib.auth.models import User
import datetime

class SimpleTest(TestCase):
    def setUp(self):
        # Create some basic test kittypes
        camera = KitType.objects.create(name='Camera', description='Time for a close up')
        cleese = KitType.objects.create(name='John Cleese', description='And now for something completely different')
        cable = KitType.objects.create(name='Cable', description='Plug me in!')

        # Create some basic kit
        Kit.objects.create(type=camera, serial='Cam 1')
        Kit.objects.create(type=camera, serial='Cam 2')
        Kit.objects.create(type=camera, serial='Cam 3')

        Kit.objects.create(type=cleese, serial='Cleese 1')
        Kit.objects.create(type=cleese, serial='Cleese 2')
        Kit.objects.create(type=cleese, serial='Cleese 3')

        Kit.objects.create(type=cable, serial='Cable 1')
        Kit.objects.create(type=cable, serial='Cable 2')
        Kit.objects.create(type=cable, serial='Cable 3')

        self.test_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    def tearDown(self):
        # Clean up db
        Booking.objects.all().delete()
        Kit.objects.all().delete()
        KitType.objects.all().delete()
        User.objects.all().delete()

    def test_booking_creation(self):

        time_period = datetime.timedelta(30)

        b = Booking()
        b.user = self.test_user
        b.start_date = datetime.datetime.now()
        b.end_date = datetime.datetime.now()+time_period
        b.save()

        items = Kit.objects.all()
        b.kits = items

        b.save()

