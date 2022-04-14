from django.forms import models

from ship.models import Shipment


class ShipmentForm(models.ModelForm):
    class Meta:
        model = Shipment
        fields = '__all__'
