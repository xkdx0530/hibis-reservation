from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='お名前')),
                ('start_at', models.DateTimeField(verbose_name='開始日時')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('menu', models.ForeignKey(on_delete=models.CASCADE, to='menus.menu', verbose_name='メニュー')),
            ],
            options={'ordering': ['start_at'],},
        ),
    ]
