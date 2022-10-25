from django.urls import path
from . import views

#app_name = 'accounts'
urlpatterns = [
    path('', views.loginPage, name='login'),
    path('logout/', views.loginPage, name='logout'),
    path('register/', views.registerPage, name='register'),
]