from django.shortcuts import render,get_object_or_404,redirect
from .models import Jobfield,Company,User,Jobseeker
from .forms import CompanyForm,Userform,Jobform,Seekerform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse


def index(request):
    return render(request,'job/index.html')

@login_required(login_url='{% url "job:login" %}')
def profile(request):
    user1 = request.user
    if user1.is_company:
        comp_obj = get_object_or_404(Company, user__username = user1)
        content ={'details': comp_obj}
        return render(request,'job/profile_for_comp.html',content)
    elif user1.is_jobseeker:
        seeker_obj = get_object_or_404(Jobseeker, user__username = user1)
        content ={'details': seeker_obj}
        return render(request,'job/profile.html',content)

def blog(request):
    if request.method == 'GET':
        status = request.GET.get('search','')
        if status == '':
            job = Jobfield.objects.all()
        else:
            job = Jobfield.objects.filter(job_category = status)
            
        return render(request,'job/blog.html',{'jobs':job})
    else:
        job=Jobfield.objects.all()
    return render(request,'job/blog.html',{'jobs':job})

def job_details(request,id):
    try:
        job_detail=Jobfield.objects.get(id=id)
    except Jobfield.DoesNotExist:
        job_detail=None
        
    return render(request,'job/blog-details.html',{'job':job_detail})

def post_a_job (request):
    if request.method == 'POST':
        form = Jobform(request.POST)
        
        if form.is_valid():
            
            Company_obj = Company.objects.get(user=request.user)
            catagory = request.POST.get('category')
            description = request.POST.get('description')
            experience = request.POST.get('experience')
            location = request.POST.get('location')
            salary = request.POST.get('salary')
            job_obj = Jobfield(job_comp = Company_obj, job_description = description,job_experience = experience, job_category = catagory , job_location = location , job_salary = salary)
            job_obj.save()
            return redirect('job:index')
        else:
            return HttpResponse(form.errors)
    else:
        form = Jobform()
    return render(request,'job/post_a_job.html',{'form':form})
    

def signup_connector(request):
    return render(request,'job/connector.html')


def comp_signup(request):
    if request.method=="POST":
        form = CompanyForm(request.POST)
        form1 = Userform(request.POST,request.FILES)
        if form.is_valid():
            image = request.FILES['profile_pic']
            name = request.POST.get('company')
            user_id = request.POST.get('username')
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
            User_obj.profile_pic = image
            User_obj.save()
            comp_obj=Company(comp_name = name,user = User_obj, comp_phoneno =phone,comp_email =email,comp_description =desc,comp_addressline1 =add1,comp_addressline2 =add2,comp_zipcode =zip1,comp_state = state,comp_country = city)
            comp_obj.save()
            return redirect('job:index')
    else:
        form = CompanyForm()
        form1 = Userform()

    return render(request,'job/company-signup.html',{'form':form,'form1':form1})

def jobseeker_signup(request):
    if request.method=="POST":
        form = Seekerform(request.POST,request.FILES)
        form1 = Userform(request.POST,request.FILES)
        if form.is_valid():
            image = request.FILES.get('profile_pic','default/download.png')
            resume = request.FILES.get('resume','default/no-image.png')
            name = request.POST.get('company')
            user_id = request.POST.get('username')
            password=request.POST.get('first_name')
            qualification = request.POST.get('additional')
            address =request.POST.get('street')
            state=request.POST.get('state')
            zip1=request.POST.get('zip')
            city=request.POST.get('city')
            phone=request.POST.get('phone')
            email=request.POST.get('your_email')
            User_obj = User(username =  user_id,is_jobseeker = True)
            User_obj.set_password(password)
            User_obj.profile_pic = image
            User_obj.save()
            seeker_obj = Jobseeker(user = User_obj,full_name = name,email = email,contact = phone ,address = address,zipcode = zip1,city = city,state = state,max_Qualification = qualification,resume = resume)
            seeker_obj.save()
            return redirect('job:index')
        else:
            User_obj.delete()
    else:
        form = Seekerform()
        form1 = Userform()

    return render(request,'job/jobseeker_signup.html',{'form':form,'form1':form1})

def login_connector(request):
    return render(request,'job/connector_login.html')

#def comp_login(request):
    #return render(request,'job/login.html')

def comp_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('first_name')
        user = authenticate(username=username, password=password)
        if user.is_company:
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
        return render(request, 'job/comp_login.html', {})

def seeker_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('first_name')
        user = authenticate(username=username, password=password)
        if user.is_jobseeker:
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
        return render(request, 'job/seeker_login.html', {})

def logout_user(request):
    logout(request)
    return redirect('job:index')