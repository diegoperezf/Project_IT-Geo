from django.shortcuts import render
from sensorsdb.api import devices
from influxdb_client.client.flux_table import FluxStructureEncoder

def get_device(request, device_id):
    result = devices.get_device(device_id)
    if not result:
        context = {'data': None}
        return render(request, 'sensorsdb/devices.html', context)
    else:
        context = {'data': result}
        return render(request, 'sensorsdb/devices.html', context)

def get_devices(request):
    result = devices.get_device(device_id=None)
    if not result:
        context = {'data': None}
        return render(request, 'sensorsdb/devices.html', context)
    else:
        context = {'data': result}
        return render(request, 'sensorsdb/devices.html', context)

def create(request):
    context = {} # None
    return render(request, 'sensorsdb/create.html', context)

def create_device(request):
    if request.method == 'GET':
        context = {}
        return render('sensorsdb/create.html', context)
    else:
        
        device_id = request.POST['device_id_input']
        device_id = devices.create_device(device_id)
        context = {'device_id' : device_id}
        return render(request, 'sensorsdb/create.html', context)


def get_buckets(request):
    buckets = devices.get_buckets()
    buckets = buckets.buckets
    context = {'buckets' : buckets}
    return render(request, 'sensorsdb/buckets.html', context)

def auth(request):
    response = devices.create_authorization('test_id')
    return render(request, 'sensorsdb/auth.html')


def write(request):
    if request.method == 'GET':
        context =  {'device_id' : None} 
        return render(request, 'sensorsdb/write.html', context)
    else:
        device_id = request.POST['device_id_input']
        print(device_id)
        device_id = [device_id]
        #print(device_id)
        device_id = devices.write_measurements(device_id)
        print(device_id)
        context =  {'device_id' : device_id}
        return render(request, 'sensorsdb/write.html', context)


def data(request):
    if request.method == 'GET':
        context = {'data' : None}
        return render(request, 'sensorsdb/data.html', context)
    else:
        device_id = request.POST['device_id_input']
        results = devices.get_measurements(device_id)
        context = {'data' : results}
        return render(request, 'sensorsdb/data.html', context)