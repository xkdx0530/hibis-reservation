from django.db import models

class Menu(models.Model):
    CATEGORY_CHOICES = [
        ('stretch', 'ストレッチ'),
        ('esthetic', 'エステ'),
    ]

    name = models.CharField('メニュー名', max_length=100)
    category = models.CharField('カテゴリ', max_length=20, choices=CATEGORY_CHOICES)
    treatment_minutes = models.PositiveIntegerField('施術時間(分)')
    losstime_minutes = models.PositiveIntegerField('ロスタイム(分)')

    def __str__(self):
        return self.name

    @property
    def total_minutes(self):
        return self.treatment_minutes + self.losstime_minutes
