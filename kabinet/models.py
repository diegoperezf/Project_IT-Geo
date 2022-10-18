from django.db import models

# Create your models here.

class User(models.Model):
    fullname = models.CharField(max_length=25)
    username = models.CharField(max_length=10)
    email = models.CharField(max_length=30)


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    
    def __str__(self):
        return self.name
