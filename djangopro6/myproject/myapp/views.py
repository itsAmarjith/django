from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Student
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return HttpResponse('hello')


def student_create(request):

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']

        Student.objects.create(
            name=name,
            age=age,
            email=email

        )


        return redirect('student_list')

    return render(request, 'student_create.html')



def student_list(request):
    student= Student.objects.all()

    return render(request,'student_list.html', {
        'students': student
    })

def student_update(request, id):
    student = get_object_or_404(Student,id=id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.email = request.POST['email']

        student.save()

        return redirect('student_list')

    return render(request, 'student_update.html', {
        'student': student
    })




def student_delete(request,id):

    student = get_object_or_404(Student,id=id)

    student.delete()

    return redirect('student_list')






