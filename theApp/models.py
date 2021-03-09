from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, unique=True, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Bus(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    driver = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    bus_img = models.ImageField(null=True, blank=True)
    plate_no = models.CharField(max_length=200, null=True, blank=True)
    seat = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Routes(models.Model):
    STATUS = (
			('Available', 'Available'),
            ('No Available Seat', 'No Available Seat'),
			('Departed', 'Departed'),
			)
    bus = models.ForeignKey(Bus, null=True, on_delete= models.SET_NULL)
    trip = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True)
    date = models.DateTimeField(null=True)
    status = models.CharField(default="Available", max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.trip

class Booking(models.Model):
    STATUS = (
			('Active Booking', 'Active Booking'),
            ('Used Booking', 'Used Booking'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    route = models.ForeignKey(Routes, null=True, on_delete= models.SET_NULL)
    agent = models.CharField(max_length=200, null=True)
    emgergency_Contact_Name = models.CharField(max_length=200, null=True)
    emgergency_Contact_Number = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
  
    def __str__(self):
        return self.agent

class CusBooking(models.Model):
    STATUS = (
			('Active Booking', 'Active Booking'),
            ('Used Booking', 'Used Booking'),
		)
    route = models.ForeignKey(Routes, null=True, on_delete= models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    emgergency_Contact_Name = models.CharField(max_length=200, null=True)
    emgergency_Contact_Number = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
