from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm

# Create your views here.
def index(request):
    return HttpResponse('hello')


def student_register(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save()
            return render(request,'sucess.html',{'student': student})

    else:
        form = StudentForm()

    return render(request,'student_form.html',{'form': form})


