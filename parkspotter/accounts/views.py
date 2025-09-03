from django.shortcuts import render,redirect
from .models import UserRegistration
from django.contrib import messages
# Create your views here.

def user_registration(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
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
        if UserRegistration.objects.filter(phone=phone).exists():
            messages.error(request, "Phone number is already registered.")
            return redirect('user_registration')

        UserRegistration.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            password=password
        )
        messages.success(request, "Registration successful.")
        return redirect('login')
    return render(request, 'user_registration.html')
