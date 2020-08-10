# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
import pytz

from django.shortcuts import render, redirect 
from invoice.models import Invoice
from events.models import Events
from passenger.models import Passenger
from django.views.generic.edit import CreateView
from .forms import InvoiceForm
# Create your views here.



class InvoiceCreateView(CreateView):

    model = Invoice
    success_url = "/dashboard/"
    fields = ['description', 'hours','rate', 'miles', 'passenger', ]


def invoice_create(request):
    
    template = 'invoice/invoice_form.html'
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        description= form.cleaned_data.get("description")
        hours= form.cleaned_data.get("hours")
        rate= form.cleaned_data.get("rate")
        miles= form.cleaned_data.get("miles")
        passenger= form.cleaned_data.get("passenger")
        passenger_data_model = Passenger.objects.get(id=passenger.id)
        pick_up_day_s = ""
        pick_up_day = ""
        pick_up_time = ""
        pick_up_time_s = ""
        date_time_joined = ""
        print(passenger_data_model.pick_up_date)
        pick_up_date = passenger_data_model.pick_up_date
        pick_up_time =passenger_data_model.pick_up_time
        tzinfo=pytz.UTC

        def get_datetime():
            return '%s %s' % (pick_up_date, pick_up_time)

        date_time_joined = get_datetime()
        pick_up_date = date_time_joined
        lista = [description, hours, miles, passenger, rate, pick_up_date ]
        for x in lista:
            print(x)
        
        new_event = Events.objects.create(event_name=description, start_date=pick_up_date,  event_type="Creado desde invoice")
        new_event.save()

        return redirect('/dashboard')
    context = {"form": form}
    return render(request, template, context)