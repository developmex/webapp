# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import Customer, Service, Order
from .models import Medical_condition

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class Medical_conditionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Medical_condition, Medical_conditionAdmin)

class ServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Service, ServiceAdmin)



class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order, OrderAdmin)