from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    
def __str__(self):
    return self.name
    
