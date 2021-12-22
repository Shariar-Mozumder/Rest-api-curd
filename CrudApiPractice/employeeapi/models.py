from django.db import models

# Create your models here.
class Employee(models.Model):
    full_name = models.CharField(max_length=30)
    emp_code= models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
