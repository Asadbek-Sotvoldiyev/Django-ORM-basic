from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('book/', views.book, name="book"),
    path('teacher/', views.teacher, name="teacher"),
    path('student/', views.student, name="student"),
    path('univer/', views.univer, name="univer"),
    path('cars/', views.cars, name="cars"),
]
