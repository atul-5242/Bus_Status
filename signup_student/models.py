from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    Id=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password1=models.CharField(max_length=150)
    password2=models.CharField(max_length=150)

