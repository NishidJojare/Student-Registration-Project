from django.db import models

# Create your models here.


class Course(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField() 
    
    
    def __str__(self):
        return self.name
    
    
    
class Student(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    course=models.ManyToManyField(Course,related_name='students')
    
    def __str__(self):
        return self.full_name 
    
    
    