from email import header
from email.mime import application
from time import sleep
from wsgiref import headers
from django.shortcuts import render
from django.http import JsonResponse

import json

from .models import Shipment
from .serializer import ShipmentSerailizer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

def index(request):
    return render(request, 'ship/index.html')


@api_view(['POST'])
def track_info(request):
    tracking_num = request.data['tracking']
    print(tracking_num)
    data = Shipment.objects.get(tracking_number=tracking_num)
    serializer = ShipmentSerailizer(data)
    print(serializer.data)
    return Response(serializer.data)
