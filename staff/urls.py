from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('my-home/', views.staff_home, name='st-home'),
    path('registration/', views.registration, name='pt-reg'),
    path('appointments/', views.appointments, name='app-list'),
    path('patient_search/', views.pt_search, name='pt-search'), 
    path('staff/', views.staff_list, name = 'staff-list'),
    path('profile/', views.profile, name="staff-prof")
]
