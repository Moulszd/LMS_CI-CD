from datetime import timezone
from django.db import models
import course

# Create your models here.

# mawloud fist models 

class BaseModel(models.Model):
    created_at = models.TimeField(default=timezone.datetime.now())

class Student(BaseModel):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),   
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    enrollment_id = models.CharField(max_length=50, unique=True)