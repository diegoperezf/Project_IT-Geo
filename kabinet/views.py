from multiprocessing.reduction import send_handle
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from kabinet.models import Sensor
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from decimal import *
# Create your views here.

def UsersView(request):
    return render(request, "kabinet/users.html")

def SensorsView(request):
    sensor_list = Sensor.objects.all()
    return render(request, "kabinet/sensors.html", {"sensor_list" : sensor_list})

def NewSensor(request):
    if request.method == 'POST':
        body = json.loads(request.body("utf-8"))
        print(body)
        nName = body['name'] 
        nLon = Decimal(body['lon'])
        nLat = Decimal(body['lat'])
        print(nName, nLon, nLat)
        Sensor.objects.create(name=nName, lon=nLon, lat=nLat)
        return JsonResponse({'success': 1, 'message': 'Sensor succesfully inserted'})
        

class DetailView(generic.DetailView):
    model = Sensor
    template_name = 'kabinet/detail.html'


