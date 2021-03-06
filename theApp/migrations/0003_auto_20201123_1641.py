# Generated by Django 3.0 on 2020-11-23 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='agent',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='CusBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('emg_name', models.CharField(max_length=200, null=True)),
                ('emg_phone', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('Active Booking', 'Active Booking'), ('Used Booking', 'Used Booking')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='theApp.Customer')),
                ('route', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='theApp.Routes')),
            ],
        ),
    ]
