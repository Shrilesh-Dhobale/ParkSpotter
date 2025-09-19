from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import NewEntry
from django.contrib import messages
from datetime import datetime




# Create your views here.

@login_required
def new_entry(request):
    if request.method == 'POST':
        plate_number = request.POST.get('plateNumber')
        vehicle_type = request.POST.get('vehicleType')
        entry_time = request.POST.get('entryTime')
        exit_time = request.POST.get('exitTime')
        is_paid = request.POST.get('isPaid') == 'on'

        if not plate_number or not vehicle_type or not entry_time:
            messages.error(request, "Please fill all required fields.")
            return redirect('new_entry')
        
        entry_time_parsed = parse_datetime(entry_time)
        

        entry = NewEntry.objects.create(
            plate_number=plate_number,
            vehicle_type=vehicle_type,
            entry_time=entry_time_parsed,
        
            is_paid=is_paid
        )

        if entry.is_paid:
            messages.success(request, "Entry paid and added successfully!")
            return redirect('recipt', entry_id=entry.id)
        else:
            messages.success(request, "Entry added successfully! Payment pending.")
            return redirect('new_entry') 

    return render(request, 'new_entry.html')
    
