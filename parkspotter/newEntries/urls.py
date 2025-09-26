from django.urls import path
from . import views

urlpatterns = [
    path('new_entry/', views.new_entry, name='new_entry'),
]