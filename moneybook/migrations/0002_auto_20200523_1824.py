# Generated by Django 2.2.9 on 2020-05-23 09:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('moneybook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='inday',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='入金日'),
        ),
        migrations.AlterField(
            model_name='spending',
            name='useday',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='使用日'),
        ),
    ]