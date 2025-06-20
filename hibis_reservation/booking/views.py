from datetime import datetime, time, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Booking
from .forms import BookingForm

START_HOUR = 10
END_HOUR = 22
INTERVAL = 15  # minutes


def index(request):
    date_str = request.GET.get('date')
    if date_str:
        target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    else:
        target_date = datetime.now().date()
    bookings = list(Booking.objects.filter(start_at__date=target_date))
    slots = []
    current = datetime.combine(target_date, time(hour=START_HOUR))
    end_of_day = datetime.combine(target_date, time(hour=END_HOUR))
    while current < end_of_day:
        slot_end = current + timedelta(minutes=INTERVAL)
        free = True
        for b in bookings:
            if not (b.end_at <= current or b.start_at >= slot_end):
                free = False
                break
        slots.append({'time': current.time(), 'free': free})
        current += timedelta(minutes=INTERVAL)
    return render(request, 'booking/index.html', {'date': target_date, 'slots': slots})


def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')
            except Exception as e:
                form.add_error(None, e)
    else:
        initial = {}
        if 'date' in request.GET and 'time' in request.GET:
            initial['date'] = request.GET['date']
            initial['time'] = request.GET['time']
        form = BookingForm(initial=initial)
    return render(request, 'booking/booking_form.html', {'form': form})


@staff_member_required
def booking_list(request):
    bookings = Booking.objects.all().order_by('start_at')
    return render(request, 'booking/booking_list.html', {'bookings': bookings})


@staff_member_required
def booking_cancel(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'booking/booking_cancel_confirm.html', {'booking': booking})
