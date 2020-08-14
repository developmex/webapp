from django import forms
from .models import Invoice
from .models import Passenger


class DateInput(forms.DateInput):
    input_type = 'date'


"""
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

"""

class InvoiceForm(forms.Form):
    appointment_id = forms.CharField(max_length=255,  )
    appointment_name = forms.CharField(max_length=255, )
    start_date = forms.DateTimeField(widget=DateInput)
    end_date = forms.DateTimeField(widget=DateInput)
    appointment_type = forms.CharField(max_length=10,  )
    invoice = forms.CharField(max_length=10, )
    passenger = forms.CharField(max_length=10, )
   
    