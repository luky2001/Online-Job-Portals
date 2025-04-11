from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('register/',views.register,name="register"),
    path('login_page/',views.login_page,name="login_page"),
    path('logout_page/',views.logout_page,name='logout_page'),
    path('rec_profile/',views.rec_profile,name='profile'),
    path('view_profile/',views.view_profile,name="view_profile"),
    path('update_rec_profile/<int:id>/',views.update_rec_profile,name="update_rec_profile"),
    path('job/',views.job,name='job'),
    path('show/',views.show,name='show'),
    path('job_update/<int:id>/',views.job_update,name="job_update"),
    path('job_delete/<int:id>/',views.job_delete,name="job_delete"),
    path('condidate_register',views.condidate_register,name='condidate_register'),
    path('condidate_login/',views.condidate_login,name='condidate_login'),
    path('condidate_dashboard/',views.condidate_dashboard,name='condidate_dashboard'),
    path('condidate_logout/',views.condidate_logout,name='condidate_logout'),

  
]
