# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Appointments(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    appointment_name = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    appointment_type = models.CharField(max_length=10, null=True, blank=True)
    invoice = models.CharField(max_length=10, null=True, blank=True)
    passenger = models.CharField(max_length=10, null=True, blank=True)

    
    @property
    def appointment_prom(self):
        return '%s %s' % (self.appointment_id, self.invoice)


    def __str__(self):
        return str(self.appointment_prom)

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
