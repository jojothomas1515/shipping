from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Package, Sender, Reciever
from .serializer import ShipmentSerializer, SenderSerializer, RecieverSerializer


# Create your views here.

def index(request):
    return render(request, 'ship/index.html')


@api_view(['POST'])
def track_info(request):
    try:
        tracking_num = request.data['tracking']
        print(tracking_num)
        package = Package.objects.get(tracking_number=tracking_num)
        sender = Sender.objects.get(package__tracking_number=tracking_num)
        reciever = Reciever.objects.get(package__tracking_number=tracking_num)
        package_serializer = ShipmentSerializer(package)
        sender_serializer = SenderSerializer(sender)
        reciever_serializer = RecieverSerializer(reciever)
        result: dict = {}
        result['package'] = package_serializer.data
        result['sender'] = sender_serializer.data
        result['receiver'] = reciever_serializer.data
    except Exception as e:
        return Response(str(e), status=404)

    return Response(result)


def tracking_page(request):
    return render(request, "ship/trackingpage.html")
