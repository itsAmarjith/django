from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .models import Product
from .models import School

# Create your views here.
def index(request):
    return HttpResponse("hello Amarjith")

def htmlpro(request):
    return render(request,'index.html')


def htmlmod(request):
    stud=Student.objects.all()
    return render(request,'table.html',{'stud':stud})



def htmlmodel(request):
    stud=Product.objects.all()
    return render(request,'table.html',{'stud':stud})





def htmlmodel(request):
    stud=School.objects.all()
    return render(request,'table.html',{'stud':stud})