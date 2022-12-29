from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('home', views.doctor_home, name='dr_home'), 
    path('profile', views.profile, name='dr_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('appointments/', views.my_appointments, name='my-appointments'),
    path('patients/',views.patient_search,name='search-pt'),
    path('change_password',views.change_password,name='change_pswd')
]