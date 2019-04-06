from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Jobfield,Company
from .forms import CompanyForm
# Create your views here.
def index(request):
    return render(request,'job/index.html')

def blog(request):
    job=Jobfield.objects.all()
    return render(request,'job/blog.html',{'jobs':job})

def job_details(request,id):
    try:
        job_detail=Jobfield.objects.get(id=id)
    except Jobfield.DoesNotExist:
        job_detail=None
        
    return render(request,'job/blog-details.html',{'job':job_detail})

def signup_connector(request):
    return render(request,'job/connector.html')


def comp_signup(request):
    if request.method=="POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            name=request.POST.get('company')
            user_id=request.POST.get('username')
            password=request.POST.get('first_name')
            desc=request.POST.get('additional')
            add1=request.POST.get('street')
            add2=request.POST.get('Address')
            state=request.POST.get('state')
            zip1=request.POST.get('zip')
            city=request.POST.get('city')
            phone=request.POST.get('phone')
            email=request.POST.get('your_email')
            comp_obj=Company(comp_name =name,comp_username =user_id,comp_password =password,comp_phoneno =phone,comp_email =email,comp_description =desc,comp_addressline1 =add1,comp_addressline2 =add2,comp_zipcode =zip1,comp_state =state,comp_country =city)
            comp_obj.save()
            return HttpResponse('<h1>Success!</h1>')
    else:
        form = CompanyForm()

    return render(request,'job/company-signup.html',{'form':form})
