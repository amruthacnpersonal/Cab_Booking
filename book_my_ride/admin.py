# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from book_my_ride.models import User, Customer, Driver, Car, Location, Cab_Booking, Ride_Details

# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Location)
admin.site.register(Cab_Booking)
admin.site.register(Ride_Details)
