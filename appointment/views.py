# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from appointment.models import Appointments
# Create your views here.


from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


class AppointmentDetailView(DetailView):

    model = Appointments
    fields = '__all__'
    success_url = "/dashboard/"



class AppointmentCreateView(CreateView):

    model = Appointments
    fields = '__all__'
    success_url = "/dashboard/"

class AppointmentListView(ListView):

    model = Appointments
    fields = '__all__'
    success_url = "/dashboard/"

class CreateUpdateView(SingleObjectTemplateResponseMixin, ModelFormMixin,
        ProcessFormView):
    model = Appointments
    fields = '__all__'  

    def get_object(self, queryset=None):
        try:
            return super(CreateUpdateView,self).get_object(queryset)
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CreateUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CreateUpdateView, self).post(request, *args, **kwargs)


def appointment(request):
    all_appointments = Appointments.objects.all()
    get_appointment_types = Appointments.objects.only('appointment_type')

    if request.GET:
        appointment_arr = []
        if request.GET.get('appointment_type') == "all":
            all_appointments = Appointments.objects.all()
        else:
            all_appointments = Appointments.objects.filter(appointment_type__icontains=request.GET.get('appointment_type'))

        for i in all_appointments:
            appointment_sub_arr = {}
            appointment_sub_arr['title'] = i.appointment_name
            start_date = datetime.strptime(str(i.start_date.date()), "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
            end_date = datetime.strptime(str(i.end_date.date()), "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
            appointment_sub_arr['start'] = start_date
            appointment_sub_arr['end'] = end_date
            appointment_arr.append(appointment_sub_arr)
        return HttpResponse(json.dumps(appointment_arr))

    context = {
        "appointments": all_appointments,
        "get_appointment_types": get_appointment_types,

    }
    return render(request, 'appointment/calendar.html', context)