from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.forms.widgets import EmailInput

from web.models import Subscribe


class SubscribeForm(ModelForm):

    class Meta:
        model = Subscribe
        fields = "__all__"
        widgets = {
            "email" : EmailInput(attrs={"placeholder" : "Enter Your Email"}),
        }