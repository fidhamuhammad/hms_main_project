from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'common/homepage.html')

def user_type(request):
    return render(request,'common/user_type.html')    
 
def about(request):
    return render(request,'common/about.html')

def contact(request):
    return render(request,'common/contact.html')

def dept(request):
    return render(request,'common/department.html')

def service(request):
    return render(request,'common/service.html')

def login(request):
    return render(request,'common/login.html')

def dept_single(request):
    return render(request,'common/department_single.html')

def doctor_single(request):
    return render(request,'common/doctor_single.html')

def doctor(request):
    return render(request,'common/hms_doctor.html')






