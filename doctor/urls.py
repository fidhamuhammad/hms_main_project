from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('my-home/', views.dr_home, name='dr-home'), 
    path('dr-profile/', views.dr_profile, name='dr-pro'),
    path('edit-dr-profile/', views.edit_dr_profile, name='edit-pro'),
    path('appointments/', views.my_appointments, name='my-appointments'),
    path('patients/',views.patient_search,name='search-pt'),
    path('change_password/',views.chg_pwd,name='chg-pwd')
]