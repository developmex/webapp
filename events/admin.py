# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Events


class EventsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Events, EventsAdmin)

# Register your models here.
