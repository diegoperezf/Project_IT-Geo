from django.urls import path
from . import views

app_name = 'kabinet'
urlpatterns = [
    path('', views.UsersView, name='users'),
    path('sensors/', views.SensorsView, name='sensors'),
    path('sensors/<name>/', views.DetailView.as_view(), name='detail'),
    path('sensors/newSensor/', views.NewSensor, name='newSensor')
]
