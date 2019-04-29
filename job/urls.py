from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
app_name='job'
urlpatterns = [
    path('',views.index,name='index'),
    path('job/', views.blog, name='blog'),
    path('job-details/<int:id>/',views.job_details, name='job_details'),
    path('post_a_job/',views.post_a_job,name = 'post_a_job'),
    path('signup/',views.signup_connector,name='signup'),
    path('signup/company/',views.comp_signup, name='comp_signup'),
    path('signup/jobseeker/',views.jobseeker_signup, name='jobseeker_signup'),
    path('login/',views.login_connector,name='login'),
    path('login/company/',views.comp_login,name='comp_login'),
    path('login/jobseeker/',views.seeker_login,name='seeker_login'),
    path('logout/',views.logout_user,name = 'logout_user'),
    path('profile/',views.profile,name = 'profile'),
    path('edit_profile/',views.edit_profile,name = 'edit_profile'),
    path('companies/',views.company,name = 'company'),
    path('company_detail/<int:id>/',views.company_details,name = 'company_details'),
    path('apply/<int:id>',views.apply_for_job,name = 'apply_for_job'),
    path('comp_dash/',views.comp_dash, name='comp_dash'),
    path('comp_dash/candidates/<int:id>/',views.candidates, name='candidates'),
    path('comp_dash/candidates_profile/<int:job_id>/<int:id>/',views.candidate_profile, name='candidate_profile'),
    path('selected_conformation/<int:job_id>/<int:id>/',views.selected_send_mail,name='selected_send_mail'),
    path('subscribe', views.subscribe, name='subscribe'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)