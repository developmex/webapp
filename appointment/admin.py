# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Appointments

# Register your models here.
class AppointmentsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointments, AppointmentsAdmin)

# Register your models here.