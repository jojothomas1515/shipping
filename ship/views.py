from email import header
from email.mime import application
from time import sleep
from wsgiref import headers
from django.shortcuts import render
from django.http import JsonResponse

import json

from .models import Package, Sender, Reciever
from .serializer import ShipmentSerializer, SenderSerializer, RecieverSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

def index(request):
    return render(request, 'ship/index.html')


@api_view(['POST'])
def track_info(request):
    tracking_num = request.data['tracking']
    print(tracking_num)
    package = Package.objects.get(tracking_number=tracking_num)
    sender = Sender.objects.get(package__tracking_number=tracking_num)
    reciever = Reciever.objects.get(package__tracking_number=tracking_num)
    package_serializer = ShipmentSerializer(package)
    sender_serializer = SenderSerializer(sender)
    reciever_serializer = RecieverSerializer(reciever)
    result = {}
    result['package'] = package_serializer.data
    result['sender'] = sender_serializer.data
    result['receiver'] = reciever_serializer.data
    print(result)

    return Response(result)


def tracking_page(request):
    return render(request, "ship/trackingpage.html")
