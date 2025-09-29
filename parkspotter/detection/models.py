from django.db import models

class DetectedPlate(models.Model):
    """
    Represents a license plate detected by the system.
    """
    plate_number = models.CharField(max_length=15, unique=True, help_text="The detected license plate number.")
    timestamp = models.DateTimeField(auto_now_add=True, help_text="The date and time when the plate was first detected.")

    def __str__(self):
        return self.plate_number