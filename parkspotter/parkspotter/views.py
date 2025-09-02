from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import UserRegistration
def index(request):
    data={
        'title': 'Dashboard'
    }
    return render(request, 'index.html', context=data)

def new_entry(request):
    return render(request, 'new_entry.html')

def login(request):
    return render(request, 'login.html')

def recipt(request):
    return render(request, 'recipt.html')

def user_registration(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('user_registration')
        if UserRegistration.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('user_registration')
        

def earning_report(request):
    return render(request, 'earning_report.html')