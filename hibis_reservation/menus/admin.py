from django.contrib import admin
from .models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'treatment_minutes', 'losstime_minutes')
    list_filter = ('category',)
