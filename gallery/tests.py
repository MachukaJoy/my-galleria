from django.test import TestCase
from .models import Photos,Location,Category

# Create your tests here.

class LocationTestClass(TestCase):
  def setUp(self):
    self.Kilifi = Location(location_name='Kilifi')

  def test_instance(self):
    self.assertTrue(isinstance(self.Kilifi, Location))

  def test_save_method(self):
    self.Kilifi.save_location_name()

class PhotosTestClass(TestCase):
  def setUp(self):
    self.car_photo = Photos(photo_name ='mum' , photo_description= 'My mother' , photo_location ='Kilifi' photo_category ='family' photo ='image.jpeg')

    self.new_photo = photo(name = )