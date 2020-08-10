# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from  passenger.models import Passenger
from events.models import Events
# Create your models here.
class Invoice(models.Model):
    description = models.CharField(max_length=50)
    hours= models.CharField(max_length=100)
    rate= models.CharField(max_length=100)
    miles = models.CharField(max_length=6)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    new_event = Events.objects.all()
    

    def __unicode__(self):

        return self.description