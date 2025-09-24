"""
URL configuration for parkspotter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.index, name='dashboard'),#Site url
    path('', include('newEntries.urls'), name='new_entry'),#New entry url

    path('receipt/', include('receipts.urls'), name='receipt'),#Receipt url
    path('earning_report/', views.earning_report, name='earning_report'),#Earning report urlit
    path('accounts/', include('accounts.urls')), # Include accounts app URLs
    path('', include('accounts.urls')),#Django auth urls
    
]
    
