from django import  forms
from Emp.models import Emp

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = "__all__"
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': "First Name"}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Mobile'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmpForm, self).__init__(*args, **kwargs)
        self.fields['department'].empty_label = 'Select'