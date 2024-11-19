from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Customer, Parcel
from .forms import ParcelForm
from django.views.decorators.csrf import csrf_exempt
import datetime

def search_customer(request):
    phone = request.GET.get('phone', '')
    if phone:
        try:
            customer = Customer.objects.get(phone=phone)
            return JsonResponse({
                'name': customer.name,
            })
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'})
    return JsonResponse({})

@csrf_exempt
def save_parcel(request):
    if request.method == "POST":
        data = request.POST
        customer, _ = Customer.objects.get_or_create(phone=data['phone'], defaults={'name': data['name']})
        parcel = Parcel.objects.create(
            customer=customer,
            address=data['address'],
            cod=data.get('cod', 'off') == 'on',
            cod_amount=data.get('cod_amount', 0) or None
        )
        parcel.cod_charge = parcel.calculate_cod_charge()
        parcel.save()
        return JsonResponse({'success': True, 'id': parcel.id})
    return JsonResponse({'error': 'Invalid request'})

def parcels_by_date(request, date):
    parcels = Parcel.objects.filter(date=date)
    data = [{'id': p.id, 'customer': p.customer.name, 'address': p.address, 'cod': p.cod,
             'cod_amount': p.cod_amount, 'cod_charge': p.cod_charge} for p in parcels]
    return JsonResponse({'parcels': data})
