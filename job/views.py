from django.shortcuts import render,get_object_or_404
from .models import Jobfield,Company
# Create your views here.
def index(request):
    return render(request,'job/index.html')

def blog(request):
    job=Jobfield.objects.all()
    return render(request,'job/blog.html',{'jobs':job})

def job_details(request):
    return render(request,'job/blog-details.html')