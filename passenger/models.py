# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from transporte.models import Medical_condition




OPTIONS_TRIP = (
    ('1', 'One way'),
    ('2', 'Two way'),

)
# Create your models here.
class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    room = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    pick_up_adress = models.CharField(max_length=100)
    reciving_facility =  models.CharField(max_length=100)
    reason_for_transfer = models.CharField(max_length=100)
    passenger_information = models.CharField(max_length=100)
    pick_up_date = models.DateField(default=datetime.now, null=True)
    pick_up_time = models.TimeField(null=True )
    appointment_time = models.TimeField( null=True)

    trip = models.CharField(max_length=1, choices=OPTIONS_TRIP, null=True)
    name_and_contact_informtion = models.CharField(max_length=100, )
    proof_of_service = models.CharField(max_length=100, )
    medical_condition = models.ForeignKey(Medical_condition, on_delete=models.CASCADE)
    does_patient_requiere_special_equipment = models.CharField(max_length=100, )
    physical_condition = models.CharField(max_length=100, )





    # __unicode__ on Python 2
    def __unicode__(self):

        return "%s %s" % (self.first_name, self.last_name)
