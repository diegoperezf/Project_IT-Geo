from django.urls import path
from . import views

app_name = 'sensorsdb'
urlpatterns = [
    path('devices/', views.get_devices, name='devices'),
    path('devices/<str:device_id>/', views.get_device, name='device'),
    path('buckets/', views.get_buckets, name='buckets'),
    path('auth/', views.auth, name='auth'),
    path('write/', views.write, name='write'),
    path('data/', views.data, name='data'),
    path('create/', views.create, name='create'),
    path('create_device/', views.create_device, name='create_device'),
    path('device_info/', views.info, name='device_info'),
    path('graph/', views.graph, name='graph'),

]