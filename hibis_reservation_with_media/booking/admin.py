
from django.contrib import admin
from .models import Menu, Booking

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'price')
    search_fields = ('name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'menu', 'date', 'time')
    list_filter = ('date',)
    search_fields = ('user__username',)
