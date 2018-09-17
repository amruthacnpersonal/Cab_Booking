from django.conf.urls import url, include
from .views import *

urlpatterns = [
    # url('Customer/', CustomerAPIView.as_view()),
    url('Customer/(?P<id>[0-9]+)$', CustomerAPIView.as_view()),
    url('Driver/', DriverAPIView.as_view()),
    url('Driver/(?P<id>[0-9]+)$', DriverAPIView.as_view()),
    url('car/', CarAPIView.as_view()),
    url('car/<id>', CarAPIView.as_view()),
    url('Customer/RideDetails/<id>', CustomerRideDetailsAPIView.as_view()),
    url('Driver/RideDetails/<id>', DriverRideDetailsAPIView.as_view()),
    url('Customer/booking_cab', Cab_BookingAPIView.as_view())

]
