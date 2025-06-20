from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='メニュー名')),
                ('category', models.CharField(max_length=20, choices=[('stretch', 'ストレッチ'), ('esthetic', 'エステ')], verbose_name='カテゴリ')),
                ('treatment_minutes', models.PositiveIntegerField(verbose_name='施術時間(分)')),
                ('losstime_minutes', models.PositiveIntegerField(verbose_name='ロスタイム(分)')),
            ],
        ),
    ]
