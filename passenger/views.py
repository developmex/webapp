# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
from passenger.models import Passenger, Invoice

class PassengerListView(ListView):

    model = Passenger


class PassengerDetailView(DetailView):

    model = Passenger



class PassengerCreateView(CreateView):

    model = Passenger
    fields = ['first_name','last_name',  'room',  
    'reciving_facility','reason_for_transfer','passenger_information','pick_up_date', 'pick_up_time', 'appointment_time',
    'name_and_contact_informtion','proof_of_service','medical_condition','does_patient_requiere_special_equipment','physical_condition']
    success_url = "/dashboard/"




class PassengerUpdate(UpdateView):
    model = Passenger
    fields = ['first_name','last_name',  'room', 'reciving_facility','reason_for_transfer','passenger_information','pick_up_date', 'pick_up_time', 'appointment_time','name_and_contact_informtion','proof_of_service','medical_condition','does_patient_requiere_special_equipment','physical_condition']
    success_url = "/dashboard/"
    template_name_suffix = '_update_form'



class InvoiceCreateView(CreateView):

    model = Invoice
    success_url = "/dashboard/"
    fields = ['description', 'hours','rate', 'miles', 'passenger', ]
