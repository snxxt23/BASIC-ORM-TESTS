from django.shortcuts import render
from .models import Student
from django.db import connection


# Create your views here.

def student_list_(request):
    posts = Student.objects.all()
    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request,'output.html',{'posts':posts})

def student_list(request):
    posts = Student.objects.filter(surname__startswith='alex') | Student.objects.filter(surname__startswith='kumar')
    print(posts)
    print(connection.queries)
    
    #Qobjects
    #from django.db.models import Q
    #posts = Student.objects.filter(Q(surname__startswith='alex')|Q(surname__startswith='kumar'))
    
    return render(request,'output.html',{'posts':posts})