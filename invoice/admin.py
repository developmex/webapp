# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Invoice

class InvoiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Invoice, InvoiceAdmin)

# Register your models here.