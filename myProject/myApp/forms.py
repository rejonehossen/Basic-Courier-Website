from django import forms
from .models import ParcelBooking

class ParcelBookingForm(forms.ModelForm):
    class Meta:
        model = ParcelBooking
        fields = [
            'sender_name', 
            'sender_phone', 
            'sender_address', 
            'receiver_name', 
            'receiver_phone', 
            'receiver_address', 
            'district', 
            'area', 
            'delivery_charge', 
            'cod_option', 
            'cod_amount', 
            'cod_charge', 
            'payment_option',  # New field
            'pickup_system'    # New field
        ]

    # Optional fields with validation
    cod_option = forms.BooleanField(required=False)
    cod_amount = forms.DecimalField(required=False, max_digits=10, decimal_places=2)
    cod_charge = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    # Custom validation to ensure COD Amount is provided if COD Option is enabled
    def clean(self):
        cleaned_data = super().clean()
        cod_option = cleaned_data.get('cod_option')
        cod_amount = cleaned_data.get('cod_amount')

        if cod_option and cod_amount is None:
            raise forms.ValidationError("Please provide a COD amount if COD option is selected.")

        return cleaned_data
