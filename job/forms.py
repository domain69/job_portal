from .models import Company
from django import forms

class CompanyForm(forms.Form):
    class Meta:
        model = Company
        fields='__all__'