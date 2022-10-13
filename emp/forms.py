from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile_no', 'username', 'password','employee_code']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['email', 'password']


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = "__all__"
