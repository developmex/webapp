# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse

from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Service, Order

# Create your views here.
from django.views.generic import TemplateView

from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib import auth
from django.contrib.auth.models import User



from .utils import render_to_pdf #created in step 4


from django.contrib.auth import authenticate, login

def login(request):
    if request.user.is_authenticated():
        return redirect("/dashboard")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect("/login")

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'transporte/login.html')


def logout(request):
    auth.logout(request)
    return render(request,'transporte/logout.html')


def dashboard(request):
    user = get_object_or_404(User, id=request.user.id)
    return render(request, 'transporte/dashboard.html', {'user': user})


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        data = {

             'customers': customers,
        }
        pdf = render_to_pdf('transporte/pdf_old.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class IndexView(TemplateView):
    template_name = "index.html"

class CustomerListView(ListView):

    model = Customer


class CustomerDetailView(DetailView):

    model = Customer



class CustomerCreateView(CreateView):
    model = Customer
    fields = ['first_name','last_name',  'room',  'pick_up_facility',
    'reciving_facility','reason_for_transfer','passenger_information','requested_date_of_transportation',
    'name_and_contact_informtion','proof_of_service','medical_condition','does_patient_requiere_special_equipment','physical_condition']
    success_url = "/admin"

class ServiceListView(ListView):

    model = Service

class ServiceCreateView(CreateView):
    model = Customer
    success_url = "/"

class InvoiceCreateView(CreateView):
    model = Customer
    success_url = "/"

class InvoiceListView(ListView):

    model = Order