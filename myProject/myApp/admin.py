# admin.py
from django.contrib import admin
from .models import ParcelBooking

class ParcelBookingAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('sender_name', 'sender_phone', 'receiver_name', 'receiver_phone', 'date_booked', 'cod_option', 'cod_amount', 'cod_charge')

    # Fields to filter by in the list view
    list_filter = ('date_booked', 'cod_option', 'district')

    # Fields to search for in the list view
    search_fields = ('sender_name', 'sender_phone', 'receiver_name', 'receiver_phone')

    # Make sender and receiver phone fields clickable
    list_display_links = ('sender_name', 'receiver_name')

    # Ordering the list view by the date booked (descending)
    ordering = ('-date_booked',)

    # Fields to display in the detail view
    fields = ('sender_name', 'sender_phone', 'sender_address', 'receiver_name', 'receiver_phone', 'receiver_address', 'district', 'area', 'delivery_charge', 'cod_option', 'cod_amount', 'cod_charge', 'date_booked')

    # Enable inline editing for the area field (if necessary)
    readonly_fields = ('date_booked',)

    # Add custom save method to calculate COD charge before saving
    def save_model(self, request, obj, form, change):
        if obj.cod_option and obj.cod_amount:
            obj.calculate_cod_charge()
        super().save_model(request, obj, form, change)

# Register the ParcelBooking model with the customized admin class
admin.site.register(ParcelBooking, ParcelBookingAdmin)
