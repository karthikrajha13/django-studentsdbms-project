from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Student
from .forms import StudentForm
from .serializers import StudentSerializer


def home(request):
    return render(request, "app/index.html")

@login_required
def search(request):

    course = request.GET.get("course", "")

    students = Student.objects.none()

    if course:

        students = Student.objects.filter(
            course__icontains=course
        )

    return render(
        request,
        "app/search.html",
        {
            "course": course,
            "students": students
        }
    )

@login_required
def students(request):

    students = Student.objects.order_by("-id")

    return render(
        request,
        "app/students.html",
        {"students": students}
    )


@login_required
def edit(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.age = request.POST.get("age")
        student.course = request.POST.get("course")

        student.save()

        messages.success(request, "Student updated successfully!")

        return redirect("students")

    return render(
        request,
        "app/edit.html",
        {
            "student": student
        }
    )


@login_required
def delete(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        student.delete()

        messages.success(request, "Student deleted successfully!")

        return redirect("students")

    return render(
        request,
        "app/delete.html",
        {
            "student": student
        }
    )


@login_required
def python_students(request):

    students = Student.objects.filter(course="Python")

    return render(
        request,
        "app/students.html",
        {
            "students": students
        }
    )


def orm_demo(request):

    print("Total Students :", Student.objects.count())
    print("Any Students :", Student.objects.exists())
    print("First Student :", Student.objects.first())
    print("Last Student :", Student.objects.last())

    return HttpResponse("Check Terminal")


@login_required
def django_form(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Student registered successfully!")

            return redirect("students")

    else:

        form = StudentForm()

    return render(
        request,
        "app/djangoform.html",
        {
            "form": form
        }
    )


def signup(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():

            messages.error(request, "Username already exists.")

            return redirect("signup")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account Created Successfully!")

        return redirect("login")

    return render(request, "app/signup.html")


def login_user(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect("home")

        messages.error(request, "Invalid Username or Password")

    return render(request, "app/login.html")


def logout_user(request):

    logout(request)

    messages.success(request, "Logged out successfully.")

    return redirect("login")


@api_view(["GET", "POST"])
def student_api(request):

    if request.method == "GET":

        students = Student.objects.all()

        serializer = StudentSerializer(
            students,
            many=True
        )

        return Response(serializer.data)

    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "GET":

        serializer = StudentSerializer(student)

        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = StudentSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    student.delete()

    return Response(
        {"message": "Student deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )


class StudentAPIView(APIView):

    def get(self, request):

        students = Student.objects.all()

        serializer = StudentSerializer(
            students,
            many=True
        )

        return Response(serializer.data)