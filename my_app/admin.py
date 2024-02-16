from django.contrib import admin
from .models import Book, Teacher, Student, Cars

admin.site.register([Book, Teacher, Student, Cars])
