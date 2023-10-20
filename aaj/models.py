from django.db import models

class modi(models.Model):
    name = models.CharField(max_length=40)
    roll=models.IntegerField(max_length=10)
    city= models.CharField(max_length=20)

# Create your models here.
