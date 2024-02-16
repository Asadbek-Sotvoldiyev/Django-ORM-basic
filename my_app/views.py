from django.shortcuts import render
from .models import Book, Teacher, Student, University, Cars

def index(request):
    return render(request, 'my_app/index.html')

def book(request):
    books = Book.objects.all()
    return render(request,'my_app/book.html', {'books': books})

def teacher(request):
    teacher = Teacher.objects.all()
    return render(request,'my_app/teacher.html', {'teacher': teacher})

def student(request):
    student = Student.objects.all()
    return render(request,'my_app/student.html', {'student': student})

def univer(request):
    univer = University.objects.all()
    return render(request,'my_app/univer.html', {'univer': univer})

def cars(request):
    cars = Cars.objects.all()
    return render(request,'my_app/cars.html', {'cars': cars})
