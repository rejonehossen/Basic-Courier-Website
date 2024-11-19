
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', parcel_booking_view, name='parcel_booking'),
    path('search_customer/', search_customer, name='search_customer'),
    path('filter_by_date/', filter_by_date, name='filter_by_date'),
    path('bookings/', booking_list, name='booking_list'),
]

