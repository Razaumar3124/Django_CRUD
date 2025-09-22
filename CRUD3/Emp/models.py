from django.db import models

# Create your models here.
class Role(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

class Emp(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=30)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

