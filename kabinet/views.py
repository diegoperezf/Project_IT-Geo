from multiprocessing.reduction import send_handle
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from kabinet.models import Sensor
from django.shortcuts import render, redirect

# Create your views here.

class UsersView(generic.ListView):
    template_name = 'kabinet/users.html'

#class SensorsView(generic.ListView):
#    template_name = 'kabinet/sensors.html'

def SensorsView(request):
    sensor_list = Sensor.objects.all()
    return render(request, "kabinet/sensors.html", {"sensor_list" : sensor_list})

def NewSensor(request):
    nName = request.POST('nameSensor')
    nLon = request.POST('lonSensor')
    nLat = request.POST('latSensor')
    nSensor = Sensor.objects.create(name=nName, lon=nLon, lat=nLat)
    return redirect('/kabinet/sensors/')



class DetailView(generic.DetailView):
    model = Sensor
    template_name = 'kabinet/detail.html'


