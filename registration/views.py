from django.shortcuts import render,redirect
from .models import Student,Course 
from .forms import StudentForm,CourseForm

# Create your views here.

def student_registration(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_registration_success')
    else:
        form=StudentForm()
    return render(request,'registration/student_registration.html',{'form':form})



def course_creation(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_creation_success')
        
    else:
        form=CourseForm()
        
    return render(request,'registration/course_creation.html',{'form':form})


def student_registration_success(request):
    return render(request,'registration/registration_success.html')


def course_creation_success(request):
    return render(request,'registration/course_success.html')


def course_list(request):
    courses=Course.objects.all()
    return render(request,'registration/course_list.html',{'courses':courses})
            


def student_list(request):
    students=Student.objects.all()
    return render(request,'registration/student_list.html',{'students':students})
            


