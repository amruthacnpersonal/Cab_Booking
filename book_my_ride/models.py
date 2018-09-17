# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class User(models.Model):
    user_email = models.EmailField(max_length=50, primary_key=True, null=False)
    secret = models.CharField(max_length=50, null=False)


class Location(models.Model):
    loc_lang = models.DecimalField(max_digits=9, decimal_places=6)
    loc_lat = models.DecimalField(max_digits=9, decimal_places=6)


class Customer(models.Model):
    cust_id = models.BigAutoField(primary_key=True)
    cust_fname = models.CharField(max_length=30, null=False)
    cust_lname = models.CharField(max_length=30, null=False)
    cust_email = models.EmailField(max_length=40, null=False)
    cust_phoneno = models.IntegerField(null=False)
    secret = models.CharField(max_length=50, null=False)


class Driver(models.Model):
    driver_id = models.BigAutoField(primary_key=True)
    driver_fname = models.CharField(max_length=30, null=False)
    driver_lname = models.CharField(max_length=30, null=False)
    driver_email = models.EmailField(max_length=40, null=False)
    driver_phoneno = models.IntegerField(null=False)
    driver_licence_no = models.CharField(max_length=15, null=False)
    driver_address = models.TextField()
    driver_police_verfication = models.CharField(max_length=25, null=False)
    driver_years_exp = models.FloatField()
    secret = models.CharField(max_length=50, null=False)


class Car(models.Model):
    car_id = models.BigAutoField(primary_key=True)
    car_no = models.CharField(max_length=10, null=False)
    car_model = models.CharField(max_length=20, null=False)
    car_type = models.CharField(max_length=20, null=False)
    car_owner = models.CharField(max_length=40, null=False)
    car_owner_address = models.TextField(null=False)
    car_puc = models.TextField(null=False)
    car_insurance_details = models.TextField(null=False)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)


class Cab_Booking(models.Model):
    booking_id = models.BigAutoField(primary_key=True)
    cust_id = models.ForeignKey(Customer)
    driver_id = models.ForeignKey(Driver)
    source_loc = Location()
    dest_loc = Location()
    status = models.CharField(max_length=30, null=False)
    cancellation_by = models.CharField(max_length=30)
    cancellation_reason = models.TextField()


class Ride_Details(models.Model):
    ride_id = models.BigAutoField(primary_key=True)
    cust_id = models.ForeignKey(Customer)
    driver_id = models.ForeignKey(Driver)
    booking_id = models.ForeignKey(Cab_Booking, on_delete=models.CASCADE)
    ride_fare = models.IntegerField(null=False)
    parking_fare = models.IntegerField(null=False)
    toll_charges = models.IntegerField(null=False)
    payment_type = models.CharField(max_length=25, null=False)
    cust_rating = models.IntegerField(null=False)
    cust_comments = models.TextField()
    total_time = models.FloatField(null=False)
    booking_day = models.DateTimeField(null=False)
