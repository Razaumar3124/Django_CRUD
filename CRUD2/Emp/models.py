from django.db import models

# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Emp(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)