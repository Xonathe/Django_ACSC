from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        min_length=4,
        max_length=25,
        widget=forms.TextInput(attrs={"placeholder": "User", "class": "field_login"})
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "field_login"}),
        min_length=6,
        max_length=100
    )
