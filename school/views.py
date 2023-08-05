from django.shortcuts import render
from .models import Student,Teacher
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


def andquery(request):
    posts = Student.objects.filter(age="19") & Student.objects.filter(classroom="10")
    print(posts)
    print(connection.queries)
    return render(request,'output.html',{'posts':posts})

def unionquery(request):
    posts=Student.objects.all().values_list("firstname").union(Teacher.objects.all().values_list("firstname"))
    # .values_list is used to retreive a list of tuples containing specific fields from a models queryset
    print(posts)
    # print(connection.queries)
    return render (request,'output.html',{'posts':posts})