from django.urls import path
from .import views

app_name = 'school'

urlpatterns = [
    path('',views.student_list,name='student_list'),
]
