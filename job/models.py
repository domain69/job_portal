from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_company = models.BooleanField('Company Status',default=False)
    is_jobseeker = models.BooleanField('Job_seeker Status',default=False)

class Company(models.Model):
    comp_name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete = models.CASCADE,default=0)
    comp_phoneno = models.CharField(max_length=13)
    comp_email = models.EmailField(max_length=100)
    comp_description = models.CharField(max_length=300)
    comp_addressline1 = models.CharField(max_length=100)
    comp_addressline2 = models.CharField(max_length=100)
    comp_zipcode = models.CharField(max_length=20)
    comp_state = models.CharField(max_length=100)
    comp_country = models.CharField(max_length=100)

    def __str__(self):
        return self.comp_name

class Jobfield(models.Model):
    job_comp = models.ForeignKey(Company,on_delete=models.CASCADE)
    job_description = models.CharField(max_length=300)
    job_category = models.CharField(max_length=100)
    job_experience = models.CharField(max_length=20)
    job_location = models.CharField(max_length=50)
    job_salary = models.CharField(max_length=100)
    job_postedon = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.job_category

class Jobseeker (models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    contact = models.IntegerField(15)
    address = models.TextField(max_length=800)
    max_Qualification = models.CharField(max_length=150)