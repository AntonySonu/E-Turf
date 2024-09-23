from django.db import models

class Manager(models.Model):
    ManagerReg_Name = models.CharField(max_length=30)
    ManagerReg_Image = models.ImageField(upload_to="images",default="Null.jpg")
    ManagerReg_Email = models.EmailField()
    ManagerReg_PhNumber = models.IntegerField()
    ManagerReg_Password = models.CharField(max_length=12)
    ManagerReg_Experience = models.CharField(max_length=40)
    ManagerReg_Gender = models.CharField(max_length=15)
    ManagerReg_Status = models.TextField(default='Pending')

# Create your models here.
