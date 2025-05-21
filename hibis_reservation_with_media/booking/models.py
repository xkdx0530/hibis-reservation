
from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    name = models.CharField("メニュー名", max_length=100)
    description = models.TextField("説明", blank=True)
    image = models.ImageField("画像", upload_to='menu_images/', blank=True, null=True)
    duration = models.PositiveIntegerField("施術時間（分）")
    price = models.DecimalField("料金（円）", max_digits=6, decimal_places=0)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, verbose_name="お客様", on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, verbose_name="メニュー", on_delete=models.CASCADE)
    date = models.DateField("予約日")
    time = models.TimeField("予約時間")
    created_at = models.DateTimeField("作成日時", auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"

    class Meta:
        unique_together = ('date', 'time')
