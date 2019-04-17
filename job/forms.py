from .models import Company,User,Jobfield,Jobseeker
from django import forms

class CompanyForm(forms.Form):
    class Meta:
        model = Company
        fields='__all__'

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic',]

class Jobform(forms.Form):
    class Meta:
        model = Jobfield
        fields = '__all__'

class Seekerform(forms.ModelForm):
    class Meta:
        model = Jobseeker
        fields = ['resume',]


