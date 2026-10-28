from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    college=models.CharField(max_length=100)


    def __str__(self):
        return self.name




class Product(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    college=models.CharField(max_length=100)


    def __str__(self):
        return self.name



class School(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    college=models.CharField(max_length=100)


    def __str__(self):
        return self.name




 

    