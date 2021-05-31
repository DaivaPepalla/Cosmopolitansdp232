from django import forms
from django.contrib.auth.password_validation import validate_password


class ContactusForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.CharField(max_length=255)