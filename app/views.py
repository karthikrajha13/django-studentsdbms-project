from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
from .forms import StudentForm

def home(request):
    return render(request, "app/index.html")

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

def register(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        course = request.POST.get("course")

        student = Student(
            name=name,
            email=email,
            age=age,
            course=course
        )

        student.save()
        messages.success(request, "Student Saved Successfully!")
        print("Student Saved Successfully!")

    return render(request, "app/register.html")

def search(request):

    course = request.GET.get("course")

    return render(
        request,
        "app/search.html",
        {"course": course}
    )
    
def students(request):

    students = Student.objects.order_by("-id")

    return render(
        request,
        "app/students.html",
        {"students": students}
    )

def edit(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.age = request.POST.get("age")
        student.course = request.POST.get("course")

        student.save()

        return redirect("/students/")

    return render(
        request,
        "app/edit.html",
        {
            "student": student
        }
    )
    
def delete(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.delete()

        return redirect("/students/")

    return render(
        request,
        "app/delete.html",
        {
            "student": student
        }
    )
    
def python_students(request):

    students = Student.objects.filter(course="Python")

    return render(
        request,
        "app/students.html",
        {
            "students": students
        }
    )
from django.http import HttpResponse

def orm_demo(request):

    print("Total Students :", Student.objects.count())

    print("Any Students :", Student.objects.exists())

    print("First Student :", Student.objects.first())

    print("Last Student :", Student.objects.last())

    return HttpResponse("Check Terminal")

from django.shortcuts import render, redirect
from .forms import StudentForm

def django_form(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/students/")

    else:
        form = StudentForm()

    return render(request, "app/djangoform.html", {
        "form": form
    })