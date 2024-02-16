from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    region = models.CharField(max_length=2000)
    category = models.CharField(max_length=200)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
       return self.name
   
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    profession = models.CharField(max_length=2000)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
       return self.name
   
class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    major = models.CharField(max_length=2000)
    email = models.CharField(max_length=200)
    kursi = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
       return self.name
   
   
class University(models.Model):
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    rating = models.CharField(max_length=2000)
    email = models.CharField(max_length=200)
    developed = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
       return self.name
   
   
class Cars(models.Model):
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    model = models.CharField(max_length=2000)
    color = models.CharField(max_length=200)
    developed = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
       return self.name
   
    
