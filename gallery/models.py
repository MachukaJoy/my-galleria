from django.db import models

# Create your models here.
class Photos(models.Model):
    photo_name =models.CharField(max_length = 30)
    photo_description = models.TextField()
    Photo = models.ImageField(upload_to = 'images/', default='image.jpg')
    photo_location = models.ForeignKey('Location', on_delete=models.SET_NULL, default = '', null=True)
    photo_category = models.ForeignKey('Category', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.photo_name


class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name


class Category(models.Model):
    category_name = models.CharField(max_length = 30)


    def __str__(self):
        return self.category_name
