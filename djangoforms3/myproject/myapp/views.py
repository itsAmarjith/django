from django.shortcuts import render

from .forms import StudentForm

# Create your views here.



def student_register(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save()
            return render(request,'success.html',{'student': student})

    else:
        form = StudentForm()

    return render(request,'student_form.html',{'form': form})


