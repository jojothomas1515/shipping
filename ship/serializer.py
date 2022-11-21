from .models import Package, Sender, Reciever
from rest_framework import serializers


class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sender
        exclude = ['id', 'package']


class RecieverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reciever
        exclude = ['id', 'package']



class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        exclude = ['id']

        #
        # fields = [
        #     "tracking_number",
        #     "package_name", "package_id", "weight", "delivery_note", "delivery_status", "delivery_date", "date_shiped",
        #
        # ]
