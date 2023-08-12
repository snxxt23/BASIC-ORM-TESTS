from django.shortcuts import render
from .models import Student,Teacher
from django.db import connection
from django.db.models import Q



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
    print(connection.queries)
    return render (request,'output.html',{'posts':posts})


# def notquery(request):
#     posts = Student.objects.exclude(age=18) & Student.objects.exclude(age=20)
#     print(posts)
#     print(connection.queries)
    
#     return render(request,'output.html',{'posts':posts})

#Q objects
#~Q

def notquery(request):
    posts = Student.objects.filter(~Q(age__gt=19))
    print(posts)
    return render(request,'output.html',{'posts':posts})

#select and output individual fields
def selectandoutput(request):
    posts = Student.objects.filter(classroom=10).only('firstname','classroom')
    print(posts)
    print(connection.queries)
    return render(request,'output.html',{'posts':posts})

def raw_(request):
    posts = Student.objects.raw("SELECT * FROM school_student WHERE age=19")
    print(posts)
    print(connection.queries)
    return render(request,'output.html',{'posts':posts})

#bypass simple orm 
def raw(request):
    cursor=connection.cursor()
    cursor.execute("select * from school_student")
    fetch = cursor.fetchone()
    print(fetch)
    print(connection.queries)
    return render(request,'output.html',{'posts':fetch})