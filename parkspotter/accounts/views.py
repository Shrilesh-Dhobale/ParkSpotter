from django.shortcuts import render,redirect
from .models import UserRegistration
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
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
            password=make_password(password)
        )
        messages.success(request, "Registration successful.")
        return redirect('login')
    return render(request, 'user_registration.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = UserRegistration.objects.get(email=email)
            if check_password(password, user.password):
                messages.success(request, "Login successful.")
                return redirect('index') # Corrected redirect name
            else:
                raise UserRegistration.DoesNotExist
        except UserRegistration.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect('login')
    return render(request, 'login.html')
