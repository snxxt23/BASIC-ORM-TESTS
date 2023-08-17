from django.db import models

# Create your models here.
class Sample(models.Model):
    firstname = models.CharField(max_length=55)
    lastname=models.CharField(max_length=55)
    age =models.IntegerField()
    city = models.CharField(max_length=55)