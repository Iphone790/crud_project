from django import forms
from .models import Employee, User
from django.core import validators


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        }


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

