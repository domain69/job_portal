from django.shortcuts import render,get_object_or_404
from .models import Jobfield,Company
# Create your views here.
def index(request):
    return render(request,'job/index.html')

def blog(request):
    job=Jobfield.objects.all()
    return render(request,'job/blog.html',{'jobs':job})

def job_details(request,id):
    job_detail=get_object_or_404(Jobfield,id=id)
    return render(request,'job/blog-details.html',{'job':job_detail})

def comp_signup(request):
    if request.method=="POST":
        name=request.method.get('company')
        user_id=request.method.get('username')
        password=request.method.get('first_name')
        desc=request.method.get('additional')
        add1=request.method.get('street')
        add2=request.method.get('street1')
        state=request.method.get('state')
        zip1=request.method.get('zip')
        city=request.method.get('city')
        phone=request.method.get('phone')
        email=request.method.get('your_email')
        comp_obj=Company(comp_name =name,comp_username =user_id,comp_password =password,comp_phoneno =phone,comp_email =email,comp_description =desc,comp_addressline1 =add1,comp_addressline2 =add2,comp_zipcode =zip1,comp_state =state,comp_country =city)
        comp_obj.save()    
    return render(request,'job/company-signup.html')
