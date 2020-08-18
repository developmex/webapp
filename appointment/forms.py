from django import forms
from invoice.models import Invoice
from appointment.models import Appointments
from passenger.models import Passenger
from django.forms import ModelForm
class DateInput(forms.DateInput):
    input_type = 'date'
    


"""
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

"""

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AppointmentForm(forms.Form):
    appointment_id = forms.CharField(max_length=100)
    appointment_name = forms.CharField(max_length=100)
    start_date = forms.DateTimeField(widget=DateInput)
    end_date = forms.DateTimeField(widget=DateInput)
    pick_up_date = forms.DateTimeField(widget=DateInput)
    pick_up_time = forms.TimeField(widget=TimeInput)
    appointment_time = forms.TimeField(widget=TimeInput)
    appointment_type = forms.CharField(max_length=10)
    miles = forms.CharField(max_length=10)
    invoice = forms.ModelChoiceField(queryset= Invoice.objects.all())
    passenger = forms.ModelChoiceField(queryset=Passenger.objects.all())        

"""

class AppointmentForm(forms.ModelForm):
    
    
    class Meta:
        model = Appointments
        invoice = forms.ModelChoiceField(queryset= Invoice.objects.all())
        passenger = forms.ModelChoiceField(queryset=Passenger.objects.all())
        fields = ['appointment_name','start_date', 'end_date','pick_up_date','pick_up_time', 'appointment_time','appointment_type','miles', 'invoice', 'passenger']
    


        widgets ={'appointment_id':forms.TextInput(attrs={'class':'input', 'placeholder':'Appointment Id'})

        }
        appointment_id = forms.CharField(max_length=100)
        appointment_name = forms.CharField(max_length=100)
        start_date = forms.DateTimeField(widget=DateInput)
        end_date = forms.DateTimeField(widget=DateInput)
        pick_up_date = forms.DateTimeField(widget=DateInput)
        pick_up_time = forms.TimeField(widget=TimeInput)
        appointment_time = forms.TimeField(widget=TimeInput)
        appointment_type = forms.CharField(max_length=10)
        miles = forms.CharField(max_length=10)
        invoice = forms.ModelChoiceField(queryset= Invoice.objects.all())
        passenger = forms.ModelChoiceField(queryset=Passenger.objects.all())
"""


