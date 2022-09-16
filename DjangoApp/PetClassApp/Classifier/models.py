from django.db import models

# Create your models here.

class ML_Model(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    modelFile = models.FileField(upload_to='Classifier/MLModels') 
    priority = models.PositiveSmallIntegerField(null = True)
    url = models.URLField(blank=True)


class petsModel(models.Model):
    image = models.ImageField(upload_to = 'images')
    caption = models.CharField(max_length=200,default='pet')  
    def __str__(self):  
        return self.caption  