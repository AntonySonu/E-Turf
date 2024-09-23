from django.db import models
from AdminApp.models import *

class Uregister(models.Model):
    UserReg_Name = models.CharField(max_length=30)
    UserReg_Email = models.EmailField()
    UserReg_PhNumber = models.IntegerField()
    UserReg_Password = models.CharField(max_length=30)

class Feedback(models.Model):
    Feedback_Name = models.CharField(max_length=30)
    Feedback_Email = models.EmailField()
    Feedback_Subject = models.CharField(max_length=30)
    Feedback_Message = models.CharField(max_length=60)

class Booking(models.Model):
    Booking_User = models.ForeignKey(Uregister,on_delete=models.CASCADE)
    Booking_Turf = models.ForeignKey(Turfs,on_delete=models.CASCADE)
    Booking_Date = models.DateField()
    Booking_Time = models.CharField(max_length=40)
    Booking_Status = models.TextField(default="Pending")
    

    
# Create your models here.
