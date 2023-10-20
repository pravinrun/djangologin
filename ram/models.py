from django.db import models

class indore(models.Model):
    name=models.CharField(max_length=20)
    gmail=models.CharField(max_length=20)
    passw=models.CharField(max_length=20)
    mobile=models.IntegerField(null=True)
    date=models.CharField(max_length=20)

# Create your models here.
