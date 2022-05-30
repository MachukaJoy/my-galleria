from django.test import TestCase
from .models import Photos, Location, Category

# Create your tests here.

class LocationTestClass(TestCase):
  def setUp(self):
    self.Kilifi = Location(location_name='Kilifi')
    self.Kilifi.save_location_name()

  def test_instance(self):
    self.assertTrue(isinstance(self.Kilifi, Location))

  def test_save_method(self):
    self.Kilifi.save_location_name()
    Locations = Location.objects.all()
    print(Locations)
    self.assertTrue(len(Locations)==1)

  def test_delete_method(self):
    self.Kilifi.delete_location_name()
    Locations = Location.objects.all()
    print(Locations)
    self.assertTrue(len(Locations)==0)


  def tearDown(self):
    Location.objects.all().delete()

class PhotosTestClass(TestCase):
  def setUp(self):
    self.new_location = Location(location_name = 'Mombasa')
    self.new_location.save()

    self.new_category = Category(category_name = 'Adventure')
    self.new_category.save()

    self.new_pic = Photos(photo_name = 'Mum', photo_description = 'Mama bear', photo_location = self.new_location, photo_category = self.new_category, photo = 'image.jpg' )
    self.new_pic.save()

  def test_instance(self):
    self.assertTrue(isinstance(self.new_pic, Photos))

  def pic(self):
    self.new_pic.save_image()