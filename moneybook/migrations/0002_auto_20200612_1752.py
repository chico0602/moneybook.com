# Generated by Django 2.2.9 on 2020-06-12 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneybook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spending',
            old_name='data',
            new_name='date',
        ),
    ]
