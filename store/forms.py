from django import forms
from django.contrib.auth.password_validation import validate_password


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100,)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput,validators=[validate_password])
    password2 = forms.CharField(widget=forms.PasswordInput,validators=[validate_password])