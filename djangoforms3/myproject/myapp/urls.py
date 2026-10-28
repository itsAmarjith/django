from django.urls import path
from myapp import views
from myapp.views import student_register
urlpatterns = [

    path('hm',student_register,name='student_register'),
]
