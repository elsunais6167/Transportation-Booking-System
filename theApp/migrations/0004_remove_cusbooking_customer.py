# Generated by Django 3.0 on 2020-11-23 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0003_auto_20201123_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cusbooking',
            name='customer',
        ),
    ]