from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name='job'
urlpatterns = [
    path('',views.index,name='index'),
    path('job/', views.blog, name='blog'),
    path('job-details/<int:id>/',views.job_details, name='job_details'),
    path('signup/',views.signup_connector,name='signup'),
    path('signup/company/',views.comp_signup, name='comp_signup'),
    path('login/',views.login_connector,name='login'),
    #path('login/company/',auth_views.LoginView.as_view(template_name='job/login.html'),name='comp_login')
    path('login/company/',views.comp_login,name='comp_login')
]