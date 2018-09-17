from rest_framework import serializers
from models import Customer, Driver, Car, Location, Cab_Booking, Ride_Details, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_email')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('cust_id', 'cust_fname', 'cust_lname', 'cust_email', 'cust_phoneno')


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('driver_id', 'driver_fname',
                  'driver_lname',
                  'driver_email',
                  'driver_phoneno',
                  'driver_licence_no',
                  'driver_address',
                  'driver_police_verfication',
                  'driver_years_exp')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('car_id', 'car_no', 'car_model',
                  'car_type', 'car_owner',
                  'car_owner_address', 'car_puc', 'car_insurance_details')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class Cab_BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab_Booking
        fields = ('cust_id', 'driver_id', 'source_loc', 'dest_loc')


class Ride_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride_Details
        fields = ('booking_id', 'ride_fare', 'parking_fare',
                  'toll_charges', 'payment_type', 'cust_rating',
                  'cust_comments', 'total_time', 'booking_day')
