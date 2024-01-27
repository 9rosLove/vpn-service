from django import forms
from django.core.exceptions import ValidationError

from vpn.models import Site


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ("name", "url")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"},),
            "url": forms.URLInput(attrs={"class": "form-control"}),
        }
