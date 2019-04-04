from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'job/index.html')

def blog(request):
    return render(request,'job/blog.html')

def job_details(request):
    return render(request,'job/blog-details.html')