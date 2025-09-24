from django.urls import path
from . import views

urlpatterns = [
    path('<int:entry_id>/', views.receipt, name='receipt'),
]