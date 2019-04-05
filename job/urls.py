from django.urls import path
from . import views
app_name='job'
urlpatterns = [
    path('',views.index,name='index'),
    path('job/', views.blog, name='blog'),
    path('job-details/<int:id>/',views.job_details, name='job_details'),
    path('signup/',views.signup_connector,name='signup'),
    path('signup/company',views.comp_signup, name='comp_signup'),
]