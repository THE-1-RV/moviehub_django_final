from django import forms
from .models import Login

class SignupForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'email', 'password', 'cnf_password']
        widgets = {
            'password': forms.PasswordInput(),
            'cnf_password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class DeleteUserForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
