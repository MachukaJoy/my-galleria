from django.test import TestCase
from .models import Photos,Location,Category

# Create your tests here.

class PhotosTestClass(TestCase):

    # set up method
    def setUp(self):
        self.photo_location = Location(location_name = 'Nairobi')
        self.photo_location.save()
