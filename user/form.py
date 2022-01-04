from django import forms
from django.forms import fields, forms
from django.forms.models import ModelForm
from django.forms.widgets import EmailInput, PasswordInput, TextInput

from user.models import CustomUser


class CustomUserForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = "__all__"
        widgets = {
            "username" : TextInput(attrs={
                "class" : "text",
                "placeholder" : "Choose your Username"
            }),
            "email" : EmailInput(attrs={
                "class" : "text",
                "placeholder" : "Enter your Email"
            }),
            "password" : PasswordInput(attrs={
                "class" : "text",
                "placeholder" : "Create a Password"
            }),
            "confirm_password" : PasswordInput(attrs={
                "class" : "text",
                "placeholder" : "Confirm your Password"
            }),
        }