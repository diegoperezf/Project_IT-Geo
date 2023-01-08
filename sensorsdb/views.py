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


#def create():         it creates a devices... connect to kabinet
def create(request):
    return render(request, 'sensorsdb/create.html', device_id=None)


# On submit function for /create
def create_device(request):
    if request.method == 'GET':
        return render('sensorsdb/create.html', device_id=None)
    else:
        device_id = request.form.get('device_id_input', None)
        device_id = devices.create_device(device_id)
        return render(request, 'sensorsdb/create.html', device_id=device_id)


def get_buckets(request):
    buckets = devices.get_buckets()
    buckets = buckets.buckets
    context = {'buckets' : buckets}
    return render(request, 'sensorsdb/buckets.html', context)

def auth(request):
    if request.method == 'POST':
        response = devices.create_authorization('test_id')
        return render(request, 'sensorsdb/auth.html')

#@app.route('/write', methods=['GET', 'POST'])
def write(request):
    if request.method == 'GET':
        return render('sensorsdb/write.html', device_id=None)
    else:
        device_id = request.form.get('device_id_input', None)
        device_id = devices.write_measurements(device_id)
        return render(request, 'sensorsdb/write.html', device_id=device_id)


#@app.route('/data', methods=['GET', 'POST'])
def data(request):
    
    if request.method == 'GET':
        context = {'data' : None}
        return render(request, 'sensorsdb/data.html', context)
    else:
        device_id = request.form.get('device_id_input', None)
        results = devices.get_measurements(device_id)
        context = {'data' : results}
        return render(request, 'sensorsdb/data.html', context)