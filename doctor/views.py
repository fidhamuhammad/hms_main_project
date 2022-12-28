from django.shortcuts import render

# Create your views here.
def dr_home(request):
    return render(request,'doctor/doctor_home.html')

def dr_profile(request):
    return render(request,'doctor/dr_profile.html')

def edit_dr_profile(request):
    return render(request,'doctor/dr_edit_profile.html')

def my_appointments(request):
    return render(request,'doctor/my_appointments.html')

def patient_search(request):
    return render(request,'doctor/pt_search.html')

def chg_pwd(request):
    return render(request,'doctor/dr_change_pwd.html')
