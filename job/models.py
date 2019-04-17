from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    is_company = models.BooleanField('Company Status',default=False)
    is_jobseeker = models.BooleanField('Job_seeker Status',default=False)
    profile_pic = models.ImageField(upload_to='profile_pictures', blank=True)

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
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    full_name = models.CharField(max_length=80)
    email = models.CharField(max_length=40)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address = models.TextField(max_length=800)
    max_Qualification = models.CharField(max_length=150)
    resume = models.ImageField(upload_to='jobseeker_resume', blank=True)
    zipcode = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    job = models.ManyToManyField(Jobfield,default = 0)



    