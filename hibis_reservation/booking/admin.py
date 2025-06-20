from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'start_at')
    list_filter = ('start_at',)
    search_fields = ('name',)
