from multiprocessing.reduction import send_handle
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from kabinet.models import Sensor
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def UsersView(request):
    return render(request, "kabinet/users.html")

def SensorsView(request):
    sensor_list = Sensor.objects.all()
    return render(request, "kabinet/sensors.html", {"sensor_list" : sensor_list})
@csrf_exempt
def NewSensor(request):
    if request.is_ajax() and request.method == 'POST':
        nName = request.POST.get('name')
        nLon = int(request.POST.get('lon'))
        nLat = int(request.POST.get('lat'))
        Sensor.objects.create(name=nName, lon=nLon, lat=nLat)
        return redirect('kabinet:sensors')

class DetailView(generic.DetailView):
    model = Sensor
    template_name = 'kabinet/detail.html'


