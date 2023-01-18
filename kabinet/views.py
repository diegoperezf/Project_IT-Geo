from multiprocessing.reduction import send_handle
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from kabinet.models import Sensor
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from sensorsdb.api import devices
import json
import decimal
# Create your views here.

def users_view(request):
    return render(request, "kabinet/users.html")

def sensors_view(request):
    sensor_list = Sensor.objects.all()
    return render(request, "kabinet/sensors.html", {"sensor_list" : sensor_list})

def new_sensor(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode("utf-8"))
        nName = body['name'] 
        nLon = decimal.Decimal(body['lon'])
        nLat = decimal.Decimal(body['lat'])
        Sensor.objects.create(name=nName, lon=nLon, lat=nLat)
        devices.create_device(device_id=nName)
        return JsonResponse({'success': 1, 'message': 'Sensor succesfully inserted'})
        

class DetailView(generic.DetailView):
    model = Sensor
    template_name = 'kabinet/detail.html'


