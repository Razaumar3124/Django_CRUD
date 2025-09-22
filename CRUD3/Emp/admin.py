from django.contrib import admin
from Emp.models import Emp

# Register your models here.
class details(admin.ModelAdmin):
    list_display = ['firstname','lastname','mobile','email','password','role']

admin.site.register(Emp, details)