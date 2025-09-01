from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
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
            return render(request, 'user_registration.html', {'error': 'Passwords do not match.'})
        user = User.objects.create_user(username=email, email=email, password=password)
        user.profile.full_name = name
        user.profile.phone = phone
        user.save()
        return render(request, 'user_registration.html', {'success': 'User registered successfully.'})

    return render(request, 'user_registration.html')

def earning_report(request):
    return render(request, 'earning_report.html')