from django import forms
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class InputForm(forms.Form):

    name = forms.CharField(label='name')
