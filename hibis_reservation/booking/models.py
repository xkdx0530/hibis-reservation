from datetime import timedelta, datetime
from django.db import models
from django.core.exceptions import ValidationError
from menus.models import Menu

class Booking(models.Model):
    name = models.CharField('お名前', max_length=50)
    menu = models.ForeignKey(Menu, verbose_name='メニュー', on_delete=models.CASCADE)
    start_at = models.DateTimeField('開始日時')
    created_at = models.DateTimeField('作成日時', auto_now_add=True)

    class Meta:
        ordering = ['start_at']

    def __str__(self):
        return f"{self.name} {self.start_at:%Y-%m-%d %H:%M}"

    @property
    def end_at(self):
        return self.start_at + timedelta(minutes=self.menu.total_minutes)

    def clean(self):
        end_at = self.end_at
        for b in Booking.objects.exclude(id=self.id):
            if not (b.end_at <= self.start_at or b.start_at >= end_at):
                raise ValidationError('この時間はすでに予約されています。')
