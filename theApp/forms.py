from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class CreateBusForm(ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'

class RouteForm(ModelForm):
    class Meta:
        model = Routes
        fields = '__all__'

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class BookingCust(ModelForm):
    class Meta:
        model = CusBooking
        fields = '__all__'
        exclude = ['status']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class Contact(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'