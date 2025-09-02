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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.index, name='index'),#Site url
    path('new_entry/', views.new_entry, name='new_entry'),#New entry url
    path('', views.login, name='login'),#Login url
    path('recipt/', views.recipt, name='recipt'),#Recipt url
    path('user_registration/', views.user_registration, name='user_registration'),#User registration url
    path('earning_report/', views.earning_report, name='earning_report'),#Earning report urlit
    path('registration/', views.user_registration, name='registration'),#User registration url
]
