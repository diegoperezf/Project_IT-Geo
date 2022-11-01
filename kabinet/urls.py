from django.urls import path
from . import views

app_name = 'kabinet'
urlpatterns = [
    path('', views.users_view, name='users'),
    path('sensors/', views.sensors_view, name='sensors'),
    path('sensors/<name>/', views.DetailView.as_view(), name='detail'),
    path('sensors/newSensor', views.new_sensor, name='newSensor')
]
