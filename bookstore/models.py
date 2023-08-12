from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    birth_year = models.IntegerField()
    
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    order_date = models.DateField()