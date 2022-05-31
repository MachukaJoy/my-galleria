from django.test import TestCase
from .models import Photos, Location, Category

# Create your tests here.

class LocationTestClass(TestCase):
  def setUp(self):
    self.Kilifi = Location(location_name='Kilifi')
    self.Kilifi.save_location_name()

  def tearDown(self):
        Location.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.Kilifi, Location))

  def test_save_method(self):
    self.Kilifi.save_location_name()
    Locations = Location.objects.all()
    print(Locations)
    self.assertTrue(len(Locations)==1)

  def test_update_location(self):
    new_location.update_location(self.location.id,new_location_name)
    updated_location = Location.objects.filter(location_name='Kilifi')
    self.assertTrue(len(updated_location) > 0)

  def test_delete_method(self):
    self.Kilifi.delete_location_name()
    Locations = Location.objects.all()
    print(Locations)
    self.assertTrue(len(Locations)==0)


class PhotosTestClass(TestCase):
  def setUp(self):
    self.new_location = Location(location_name = 'Mombasa')
    self.new_location.save()

    self.new_category = Category(category_name = 'Adventure')
    self.new_category.save()

    self.new_pic = Photos(name = 'Mum', photo_description = 'Mama bear', photo_location = self.new_location, photo_category = self.new_category, photo = 'image.jpg' )
    self.new_pic.save()

  def tearDown(self):
    Photos.objects.all().delete()
    Location.objects.all().delete()
    Category.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.new_pic, Photos))

  def test_save_pic(self):
    self.new_pic.save_photo()
    photo = Photos.objects.all()

  def test_delete_pic(self):
    self.new_pic.save_photo()
    self.new_pic.delete_photo()

class CategoryTestClass(TestCase):

    def setUp(self):
      self.family= Category(category_name ='family')
      self.family.save_category_name()

    def tearDown(self):
      Category.objects.all().delete()


    def test_instance(self):
      self.assertTrue(isinstance(self.family, Category))

    def test_save_category(self):
      self.test_category = Category(category_name = 'friends')
      self.test_category.save_category_name()

    def test_delete_category(self):
      self.test_category = Category(category_name = 'friends')
      self.test_category.save_category_name()
      self.test_category.delete_category_name()