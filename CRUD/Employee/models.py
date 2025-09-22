from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(max_length=100,unique=True)
    emp_phone = models.CharField(max_length=15)
    emp_department = models.ForeignKey(Department, on_delete = models.CASCADE )