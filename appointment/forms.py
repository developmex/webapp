from django import forms
from invoice.models import Invoice
from appointment.models import Appointments
from passenger.models import Passenger

class DateInput(forms.DateInput):
    input_type = 'date'


"""
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

"""

class DateInput(forms.DateInput):
    input_type = 'date'

class AppointmentForm(forms.Form):
    appointment_id = forms.CharField(max_length=100)
    appointment_name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=50)
    start_date = forms.DateTimeField(widget=DateInput)
    end_date = forms.DateTimeField(widget=DateInput)
    appointment_type = forms.CharField(max_length=100)
    miles = forms.CharField(max_length=10)
    invoice = forms.ModelChoiceField(queryset= Invoice.objects.all())
    passenger = forms.ModelChoiceField(queryset=Passenger.objects.all())

