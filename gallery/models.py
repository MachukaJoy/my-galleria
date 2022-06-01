from django.db import models

# Create your models here.
class Photos(models.Model):
    name =models.CharField(max_length = 30)
    photo_description = models.TextField()
    photo = models.ImageField(upload_to = 'images/', default='image.jpg')
    photo_location = models.ForeignKey('Location', on_delete=models.SET_NULL, default = '', null=True)
    photocategory = models.ForeignKey('Category', on_delete=models.CASCADE, default='')

    def save_photo(self):
      self.save()

    def delete_photo(self):
      self.save()

    @classmethod
    def search_by_photocategory(cls,search_term):
      photo = cls.objects.filter(photocategory__category_name__icontains = search_term)
      return photo

    def update_image(self, Name=None, category=None):
        self.name = Name if Name else self.Name
        self.photocategory = category if category else self.photocategory 
        self.save()

    def __str__(self):
      return self.name


class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name

    def save_location_name(self):
        self.save()

    def delete_location_name(self):
        self.delete()

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(location_name=value)
        


class Category(models.Model):
    category_name = models.CharField(max_length = 30)

    def save_category_name(self):
        self.save()

    def delete_category_name(self):
        self.delete()

    def __str__(self):
        return self.category_name
