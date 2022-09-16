from django.db import models

class Image(models.Model):
   image = models.ImageField(upload_to = 'gallery', default = 'gallery/static/images/no-img.jpg')
   #image = models.ImageField(upload_to = 'gallery')
   name = models.CharField(max_length=200)
