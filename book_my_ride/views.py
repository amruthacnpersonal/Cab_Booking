# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from django.shortcuts import render
from serializers import CustomerSerializer, DriverSerializer, CarSerializer, Ride_DetailsSerializer, \
    Cab_BookingSerializer
from models import Customer, Driver, Car, Ride_Details
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction


# Create your views here.

class CustomerAPIView(APIView):
    def get_object(self, id):
        try:
            return Customer.objects.get(cust_id=id)
        except Customer.DoesNotExist as ex:
            return Response({"error : customer does not exist"}, status=404)

    def get(self, request, id):
        try:
            customer = self.get_object(id)
            serializer = CustomerSerializer(customer)
            return Response(serializer, status=200)
        except Customer.DoesNotExist as ex:
            return Response({"error : customer does not exist"}, status=404)

    def post(self, request):
        data = request.data
        try:
            cust_instance = Customer.objects.get(cust_email=data['cust_email'])
        except Customer.DoesNotExist as ex:
            cust_instance = None
        if cust_instance:  # and str(cust_instance.cust_email) == data['cust_email']:
            return Response({"error": 'Customer already exists'}, status=400)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CustomerRideDetailsAPIView(APIView):
    def get_object(self, id):
        try:
            return Customer.objects.get(cust_id=id)
        except Customer.DoesNotExist as ex:
            return Response({"error : customer does not exist"}, status=404)

    def get(self, request, id):
        try:
            customer = self.get_object(id)
            cust_serializer = CustomerSerializer(customer)
            rides = Ride_Details.objects.filter(cust_id=id)
            ride_serializer = Ride_DetailsSerializer(rides)
            return Response(ride_serializer.data, status=200)
            # return Response(serializer, status=200)

        except Customer.DoesNotExist as ex:
            return Response({"error : customer does not exist"}, status=404)


class DriverRideDetailsAPIView(APIView):
    def get_object(self, id):
        try:
            return Driver.objects.get(driver_id=id)
        except Driver.DoesNotExist as ex:
            return Response({"error : Driver does not exist"}, status=404)

    def get(self, request, id):
        try:
            driver = self.get_object(id)
            driver_serializer = DriverSerializer(driver)
            rides = Ride_Details.objects.filter(driver_id=id)
            ride_serializer = Ride_DetailsSerializer(rides)
            return Response(ride_serializer.data, status=200)
            # return Response(serializer, status=200)

        except Ride_Details.DoesNotExist as ex:
            return Response({"error : Ride for this driver does not exist"}, status=404)


class DriverAPIView(APIView):
    def get_object(self, id):
        try:
            return Driver.objects.get(driver_id=id)
        except Driver.DoesNotExist as ex:
            return Response({"error : driver does not exist"}, status=404)

    def get(self, request, id):
        try:
            driver = self.get_object(id)
            serializer = DriverSerializer(driver)
            return Response(serializer, status=200)
        except Driver.DoesNotExist as ex:
            return Response({"error : driver does not exist"}, status=404)

    def post(self, request):
        data = request.data
        try:
            driver_instance = Driver.objects.get(driver_email=data['driver_email'],
                                                 driver_phoneno=data['driver_phoneno'])
        except Driver.DoesNotExist as ex:
            driver_instance = None
        if driver_instance:
            return Response({"error": 'Driver already exists'}, status=400)
        serializer = DriverSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CarAPIView(APIView):
    def get_object(self, id):
        try:
            return Car.objects.get(car_no=id)
        except Car.DoesNotExist as ex:
            return Response({"error : car does not exist"}, status=404)

    def get(self, request, id):
        try:
            car = self.get_object(id)
            serializer = CarSerializer(car)
            return Response(serializer, status=200)
        except Car.DoesNotExist as ex:
            return Response({"error : car does not exist"}, status=404)

    def post(self, request):
        data = request.data
        try:
            car_instance = Car.objects.get(car_no=data['car_no'])
        except Car.DoesNotExist as ex:
            car_instance = None
        if car_instance:
            return Response({"error": 'Car already registered'}, status=400)
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class Ride_DetailsAPIView(APIView):
    def get_object(self, id):
        try:
            return Ride_Details.objects.get(ride_id=id)
        except Ride_Details.DoesNotExist as ex:
            return Response({"error : car does not exist"}, status=404)

    def get(self, request, id):
        try:
            ride = self.get_object(id)
            serializer = Ride_DetailsSerializer(ride)
            return Response(serializer, status=200)
        except Ride_Details.DoesNotExist as ex:
            return Response({"error : Ride_Details does not exist"}, status=404)


class Cab_BookingAPIView(APIView):
    def post(self, request):
        data = request.data
        try:
            with transaction.atomic():
                try:
                    cust_instance = Customer.objects.get(cust_id=data['cust_id'])
                except Customer.DoesNotExist as ex:
                    cust_instance = None
                if not cust_instance:  # and str(cust_instance.cust_email) == data['cust_email']:
                    return Response({"error": 'Customer doesnt exists'}, status=400)
                serializer = Cab_BookingSerializer(data=data)
                if serializer.is_valid():
                    obj = serializer.save()
                    obj.status = 'Confirmed'
                    obj.save()
                    return Response("message: Cab booked and with booking id " + obj.bookingid, status=201)
                return Response(serializer.errors, status=400)
        except Exception as ex:
            return Response({"error : exception in booking cab"})
