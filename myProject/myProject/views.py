# views.py
from django.shortcuts import render, redirect
from myApp.forms import ParcelBookingForm
from myApp.models import ParcelBooking
from django.http import JsonResponse
from datetime import datetime

def parcel_booking_view(request):
    booking = None
    if request.method == 'POST':
        form = ParcelBookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            if booking.cod_option:
                booking.calculate_cod_charge()
            return render(request, 'parcel_booking_success.html', {'booking': booking})  # Render success page with booking data

    else:
        form = ParcelBookingForm()

    return render(request, 'parcel_booking.html', {'form': form})

def search_customer(request):
    query = request.GET.get('query', '')
    customers = ParcelBooking.objects.filter(sender_phone__icontains=query)
    customer_data = [{'id': customer.id, 'name': customer.sender_name} for customer in customers]
    return JsonResponse({'results': customer_data})

def filter_by_date(request):
    date = request.GET.get('date', str(datetime.today().date()))
    bookings = ParcelBooking.objects.filter(date_booked=date)
    bookings_data = [{'id': booking.id, 'sender_name': booking.sender_name, 'receiver_name': booking.receiver_name, 'date_booked': booking.date_booked} for booking in bookings]
    return JsonResponse({'bookings': bookings_data})



from django.shortcuts import render
from django.db.models import Q
def booking_list(request):
    # Get filter parameters
    query = request.GET.get('q', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    # Filter bookings
    bookings = ParcelBooking.objects.all()

    if query:
        bookings = bookings.filter(
            Q(sender_name__icontains=query) |
            Q(receiver_name__icontains=query) |
            Q(sender_address__icontains=query) |
            Q(receiver_address__icontains=query)
        )

    if start_date and end_date:
        bookings = bookings.filter(date_booked__range=[start_date, end_date])

    return render(request, 'booking_list.html', {
        'bookings': bookings,
        'query': query,
        'start_date': start_date,
        'end_date': end_date,
    })