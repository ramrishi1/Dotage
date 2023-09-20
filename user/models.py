from django.db import models
from django.contrib.auth.models import User
import datetime

class Profile(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField()
    postcode = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=20)
    image=models.ImageField(upload_to='profile_image')

class Event(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    ename = models.CharField(max_length=100)
    edate = models.DateField(default=datetime.date.today)
    eaddress = models.TextField(default='')
    edesc = models.TextField()
    ecity= models.TextField(default='')
    ezip=models.CharField(max_length=10, default='')
    image=models.ImageField(upload_to='event_image', default='img/eventdefault.png', blank=True, null=True)
