from django.db import models

# Create your models here.

class Shipment(models.Model):
    tracking_number = models.CharField(max_length=50, unique=True)
    details = models.CharField(max_length=500,null=True, blank=True)
    destination = models.CharField(max_length=50,null=True, blank=True)
    current_location = models.CharField(max_length=50,null=True, blank=True)
    from_destination = models.CharField(max_length=50,null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True,null=True, blank=True)
