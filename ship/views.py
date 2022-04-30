from asyncore import read
from django.shortcuts import render
from django.http import JsonResponse
import json



# Create your views here.

def index(request):

    return render(request,'ship/index.html')

def track_info(request):
    if request.method == "POST":
        tracking_num = json.loads(request.body)['tracking']
    
        print(tracking_num)

        return JsonResponse({'success':"request successful"})


