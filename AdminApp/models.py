from django.db import models

class Locations(models.Model):
    Location_Name = models.CharField(max_length=30)
    Location_Image = models.ImageField(upload_to='images',default='null.jpg')

class Turfs(models.Model):
    Turf_Name = models.CharField(max_length=30)
    Turf_Image = models.ImageField(upload_to='images',default='null.jpg')
    Turf_Booking_price = models.IntegerField()
    Turf_Facilities = models.CharField(max_length=60)
    Turf_Location = models.CharField(max_length=30)
    Turf_Manager_Name = models.CharField(max_length=30)
    Turf_Working_time = models.CharField(max_length=30)
# Create your models here.
