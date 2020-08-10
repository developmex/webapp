# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    event_type = models.CharField(max_length=10, null=True, blank=True)
    
    @property
    def event_prom(self):
        return '%s %s' % (self.event_id, self.event_name)


    def __str__(self):
        return str(self.event_prom)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
