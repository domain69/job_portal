from django.shortcuts import render,get_object_or_404,redirect
from .models import Jobfield,Company,User
from .forms import CompanyForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponse


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
            User_obj = User(username =  user_id,is_company = True)
            User_obj.set_password(password)
            User_obj.save()
            comp_obj=Company(comp_name = name,user = User_obj, comp_phoneno =phone,comp_email =email,comp_description =desc,comp_addressline1 =add1,comp_addressline2 =add2,comp_zipcode =zip1,comp_state = state,comp_country = city)
            comp_obj.save()
            return redirect('job:index')
    else:
        form = CompanyForm()

    return render(request,'job/company-signup.html',{'form':form})

def login_connector(request):
    return render(request,'job/connector_login.html')

#def comp_login(request):
    #return render(request,'job/login.html')

def comp_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('first_name')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('job:index')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'job/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('job:index')