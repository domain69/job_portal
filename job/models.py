from django.db import models

class Company(models.Model):
    comp_name = models.CharField(max_length=30)
    comp_username = models.CharField(max_length=20)
    comp_password = models.CharField(max_length=16)
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