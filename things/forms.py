from django import forms
from .models import Thing
from django.core.validators import RegexValidator


class ThingForm(forms.ModelForm):
    class Meta:
        name = forms.CharField(label='Name')
        description = forms.Textarea(label = 'Description')
        quantity = forms.NumberInput(lable = 'Quantity')
