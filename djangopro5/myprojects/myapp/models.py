from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    image=models.ImageField(upload_to='Student/',blank=True,null=True)


    def __str__(self):
        return self.name

    