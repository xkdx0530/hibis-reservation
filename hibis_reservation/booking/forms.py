from datetime import datetime
from django import forms
from .models import Booking
from menus.models import Menu

class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))

    class Meta:
        model = Booking
        fields = ['name', 'menu', 'date', 'time']

    def save(self, commit=True):
        booking = super().save(commit=False)
        booking.start_at = datetime.combine(self.cleaned_data['date'], self.cleaned_data['time'])
        if commit:
            booking.save()
        return booking
