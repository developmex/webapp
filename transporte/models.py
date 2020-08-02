# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import User

from django.db import models

class Medical_condition(models.Model):
    condition = models.CharField(max_length=50)
    important_considerations = models.TextField(max_length=500)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.condition

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adress = models.CharField(max_length=50)
    id_number_gov = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.id_number_gov



OPTIONS_TRIP = (
    ('1', 'One way'),
    ('2', 'Two way'),

)
# Create your models here.
class Customer(models.Model):
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

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    cost_per_hour = models.CharField(max_length=100)
    cost_per_mile = models.CharField(max_length=100)

    def __unicode__(self):

        return self.service_name


class Order(models.Model):
    number_id  = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    hours = models.CharField(max_length=100)
    miles = models.CharField(max_length=100)

    def __unicode__(self):
        return self.number_id


class Invoice(models.Model):
    description = models.CharField(max_length=50)
    hours= models.CharField(max_length=100)
    rate= models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __unicode__(self):

        return self.description


