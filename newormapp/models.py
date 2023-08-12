from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Teacher(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Course(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()

class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=50)

class chapter(models.Model):
    index_number = models.IntegerField()
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=50)

