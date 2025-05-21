
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking, Menu
from .forms import BookingForm

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            if Booking.objects.filter(date=booking.date, time=booking.time).exists():
                form.add_error('time', 'この時間はすでに予約されています。')
            else:
                booking.save()
                return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})

@login_required
def booking_cancel(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'booking/booking_cancel_confirm.html', {'booking': booking})

def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'booking/menu_detail.html', {'menu': menu})

def index(request):
    return render(request, 'booking/index.html')
