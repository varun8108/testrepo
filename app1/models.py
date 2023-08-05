from django.db import models

# Create your models here.

class Details(models.Model):
    name = models.CharField('name',max_length=10)
    fathername = models.CharField('fathername',max_length=10)
    Class = models.CharField('class',max_length=10)
    age = models.IntegerField('age',max_length=10)
    image = models.ImageField('file')

    def __str__(self):
        return self.name
