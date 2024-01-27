from django import forms
from vpn.models import Site


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ["title", "url"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"},),
            "url": forms.URLInput(attrs={"class": "form-control"}),
        }
