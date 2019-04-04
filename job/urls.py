from django.urls import path
from . import views
app_name='job'
urlpatterns = [
    path('',views.index,name='index'),
    path('job/', views.blog, name='blog'),
    path('job-details/<int:id>/',views.job_details, name='job_details')
]