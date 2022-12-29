from django.shortcuts import render
from common.models import Patient
# Create your views here.
def home(request):
    patient = Patient.objects.filter(id = request.session['patient']).values('patient_name')
    pat_name = patient[0]['patient_name']
    return render(request,'patient/patient_home.html', {'pat_name' : pat_name})

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
    