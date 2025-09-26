# newEntries/views.py

# +++ ADD JsonResponse to your imports +++
from django.http import JsonResponse
# +++ ADD the json library +++
import json
from django.views.decorators.csrf import csrf_exempt # You may need this for API-style views
from django.shortcuts import render # Keep render for GET requests
from django.contrib.auth.decorators import login_required
from .models import NewEntry
from datetime import datetime

@csrf_exempt
@login_required
def new_entry(request):
    # This part handles the initial page load (a GET request)
    if request.method == 'GET':
        return render(request, 'new_entry.html')

    # This part handles the JSON data from your JavaScript (a POST request)
    if request.method == 'POST':
        try:
            # 1. Load the JSON data from the request body
            data = json.loads(request.body)
            plate_number = data.get('plateNumber')
            vehicle_type = data.get('vehicleType')
            entry_time_str = data.get('entryTime')
            is_paid = data.get('isPaid', False) # .get() is safer

            # 2. Perform validation (same as before)
            if not all([plate_number, vehicle_type, entry_time_str]):
                return JsonResponse({'error': 'Please fill all required fields.'}, status=400)

            # 3. Parse the datetime (same as before)
            try:
                entry_time_parsed = datetime.strptime(entry_time_str, '%Y-%m-%dT%H:%M')
            except (ValueError, TypeError):
                return JsonResponse({'error': 'Invalid date and time format.'}, status=400)

            # 4. Create the object
            entry = NewEntry.objects.create(
                plate_number=plate_number,
                vehicle_type=vehicle_type,
                entry_time=entry_time_parsed,
                is_paid=is_paid
            )

            # 5. Return a JSON response with the new entry's ID
            # This is what your JavaScript's 'then(data => ...)' block will receive
            if entry.is_paid:
                 return JsonResponse({'entry_id': entry.id})
            else:
                # Handle the unpaid case if needed, for now we can just return success
                # Or you could return a different value and handle it in JS
                return JsonResponse({'success': True, 'message': 'Entry created successfully.'})


        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)
        except Exception as e:
            # Catch other potential errors
            return JsonResponse({'error': str(e)}, status=500)

    # Handle other methods like PUT, DELETE etc. if necessary
    return JsonResponse({'error': 'Invalid request method.'}, status=405)