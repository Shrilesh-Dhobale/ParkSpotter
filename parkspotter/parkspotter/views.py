from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data={
        'title': 'Dashboard'
    }
    return render(request, 'index.html', context=data)

def new_entry(request):
    return render(request, 'new_entry.html')

def recipt(request):
    return render(request, 'recipt.html')

def earning_report(request):
    return render(request, 'earning_report.html')