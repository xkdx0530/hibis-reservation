
from django import forms
from .models import Booking
from django.forms.widgets import TimeInput

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['menu', 'date', 'time']
        widgets = {
            'date': forms.SelectDateWidget,
            'time': TimeInput(format='%H:%M', attrs={'type': 'time'})
        }
