from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class SearchProductHome(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control border-2 border-secondary  w-75  rounded-pill", "placeholder": "متن جستجو"}),
                           label="متن جستجو")
