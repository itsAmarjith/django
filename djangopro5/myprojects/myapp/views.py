from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.
def index(request):
    return HttpResponse("hello Amarjith")

def htmlpro(request):
    return render(request,'index.html')


def htmlmod(request):
    stud=Student.objects.all()
    return render(request,'table.html',{'stud':stud})
