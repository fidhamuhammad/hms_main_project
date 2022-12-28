from django.shortcuts import render

# Create your views here.
def p_home(request):
    return render(request,'patient/patient_home.html')

def appointment(request): # old appointment
    return render(request,'patient/appointment.html')

def confirmation(request): # old confirmation
    return render(request,'patient/confirmation.html')

def my_bookings(request):
    return render(request,'patient/my_bookings.html')

def prescriptions(request):
    return render(request,'patient/prescriptions.html')

def change_password(request):
    return render(request,'patient/pt_change-password.html')

def pt_profile(request):
    return render(request,'patient/pt-profile.html')

def register(request):
    return render(request,'patient/register.html')

def edit(request):
    return render(request,'patient/pt_edit_profile.html')

def appt_1(request):
    return render(request,'patient/appt_1.html')

def appt_2(request):
    return render(request,'patient/appt_2.html')

def appt_3(request):
    return render(request,'patient/appt_3.html')

def appt_4(request):
    return render(request,'patient/appt_4.html')

def appt_list(request):
    return render(request,'patient/appointment_list.html')
    