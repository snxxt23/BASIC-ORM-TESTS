from django.urls import path,include
from .import views

app_name = 'school'

urlpatterns = [
    path('or',views.student_list,name='student_list'),
    path('and',views.andquery,name="andquery"),
]
