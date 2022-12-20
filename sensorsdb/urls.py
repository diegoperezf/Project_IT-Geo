from django.urls import path
from . import views

app_name = 'sensorsdb'
urlpatterns = [
    path('devices/<str:device_id>/', views.get_device, name='devices'),
    path('buckets/', views.get_buckets, name='buckets'),
    path('auth/', views.auth, name='auth'),
    path('write/', views.write, name='write'),
    path('data/', views.data, name='data')
]