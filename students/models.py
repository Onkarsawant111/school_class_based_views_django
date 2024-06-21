from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
