from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            "emp_name": "Name",
            "emp_email": "Email",
            "emp_phone": "Mobile",
            "emp_department": "Department",
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['emp_department'].empty_label = "Select"