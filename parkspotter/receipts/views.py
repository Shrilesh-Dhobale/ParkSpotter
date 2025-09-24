from django.shortcuts import render,get_object_or_404
from newEntries.models import NewEntry
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def receipt(request,entry_id):
    entry=get_object_or_404(NewEntry,id=entry_id)

    rates = {
        'Bike': 30,
        'Car': 80,
        'Bus': 120,
    }
    rate = rates.get(entry.vehicle_type, 0)
    amount = rate

    context = {
        'plate_number': entry.plate_number,
        'vehicle_type': entry.vehicle_type,
        'entry_time': entry.entry_time,
        'is_paid': entry.is_paid,
        'rate': rate,
        'amount': amount,
    }
    return render(request, 'receipt.html', context)