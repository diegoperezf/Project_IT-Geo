from django.shortcuts import render
from sensorsdb.api import devices
from influxdb_client.client.flux_table import FluxStructureEncoder
# Create your views here.

def get_device(request, device_id):
    if request.method == 'POST': 
        result = devices.get_device(device_id)
        if not result:
            return render(request, 'devices.html', data=None)
        else:
            return render(request, 'devices.html', data=result)


#def get_devices():    it shows the list of devices? then it should be replaced by kabinet    
def get_devices(request):
    result = devices.get_device(device_id=None)
    if not result:
        return render(request, 'devices.html', data=None)
    else:
        return render(request, 'devices.html', data=result)


#def create():         it creates a devices... connect to kabinet
def create(request):
    return render(request, 'create.html', device_id=None)


# On submit function for /create
def create_device(request):
    if request.method == 'GET':
        return render('create.html', device_id=None)
    else:
        device_id = request.form.get('device_id_input', None)
        device_id = devices.create_device(device_id)
        return render('create.html', device_id=device_id)


#def create_device():   same

def get_buckets(request):
    if request.method == 'POST':
        buckets = devices.get_buckets()
        buckets = buckets.buckets
        return render('buckets.html', buckets=buckets)

def auth(request):
    if request.method == 'POST':
        response = devices.create_authorization('test_id')
        return render('auth.html')

#@app.route('/write', methods=['GET', 'POST'])
def write(request):
    if request.method == 'GET':
        return render('write.html', device_id=None)
    else:
        device_id = request.form.get('device_id_input', None)
        device_id = devices.write_measurements(device_id)
        return render('write.html', device_id=device_id)


#@app.route('/data', methods=['GET', 'POST'])
def data(request):
    if request.method == 'GET':
        return render('data.html', data=None)
    else:
        device_id = request.form.get('device_id_input', None)
        results = devices.get_measurements(device_id)
        return render('data.html', data=results)