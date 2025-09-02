from django.db import models

class UserRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    

    def __str__(self):
        return f"{self.full_name} ({self.email})"