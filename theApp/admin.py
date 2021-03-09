from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Bus)
admin.site.register(Booking)
admin.site.register(Routes)
admin.site.register(CusBooking)
admin.site.register(Contact)