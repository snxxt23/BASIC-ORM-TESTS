from django.db import models

# Create your models here.


class Teacher (models.Model):
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname

class Student (models.Model):
    teacher = models.ForeignKey(Teacher,null=True,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    classroom = models.IntegerField()

    def __str__(self):
        return self.firstname
