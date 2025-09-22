from django import forms
from Emp.models import Emp

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Mobile No.'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.TextInput(attrs={'placeholder': 'Enter Password'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmpForm, self).__init__(*args, **kwargs)
        self.fields['role'].empty_label = 'Select'

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=40)
    password = forms.CharField(max_length=30)