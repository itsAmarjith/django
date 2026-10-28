from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

# Create your views here.

class Register_View(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer

