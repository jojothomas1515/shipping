from .models import Shipment
from rest_framework import serializers

class ShipmentSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Shipment
        fields ='__all__'