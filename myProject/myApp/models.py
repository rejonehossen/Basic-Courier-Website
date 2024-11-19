# from django.db import models

# class ParcelBooking(models.Model):
#     # Sender Details
#     sender_name = models.CharField(max_length=255)
#     sender_phone = models.CharField(max_length=15)
#     sender_address = models.CharField(max_length=255, default="Chittagong Road, Narayanganj")

#     # Receiver Details
#     receiver_name = models.CharField(max_length=255)
#     receiver_phone = models.CharField(max_length=15)
#     receiver_address = models.CharField(max_length=255)
#     district = models.CharField(max_length=100)
#     area = models.CharField(max_length=100, blank=True, null=True)

#     # Delivery Details
#     delivery_charge = models.DecimalField(max_digits=10, decimal_places=2)
#     cod_option = models.BooleanField(default=False)
#     cod_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     cod_charge = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

#     # Payment and Pickup Details
#     PAYMENT_OPTIONS = [
#         ('cash', 'Cash'),
#         ('to_pay', 'To Pay'),
#     ]
#     payment_option = models.CharField(
#         max_length=10,
#         choices=PAYMENT_OPTIONS,
#         default='cash'
#     )

#     PICKUP_SYSTEM = [
#         ('home_delivery', 'Home Delivery'),
#         ('office_delivery', 'Office Delivery'),
#     ]
#     pickup_system = models.CharField(
#         max_length=15,
#         choices=PICKUP_SYSTEM,
#         default='office_delivery'
#     )

#     # Date Details
#     date_booked = models.DateField(auto_now_add=True)

#     # Methods
#     def calculate_cod_charge(self):
#         """Calculate COD charge based on the COD amount."""
#         if self.cod_option and self.cod_amount is not None:
#             if self.cod_amount <= 1000:
#                 self.cod_charge = 20
#             elif self.cod_amount <= 2000:
#                 self.cod_charge = 30
#             elif self.cod_amount <= 3000:
#                 self.cod_charge = 40
#             else:
#                 self.cod_charge = (self.cod_amount // 1000) * 10
#             self.save()

#     def __str__(self):
#         return f"Parcel booked by {self.sender_name} for {self.receiver_name}"



from django.db import models

class ParcelBooking(models.Model):
    # Sender Details
    sender_name = models.CharField(max_length=255)
    sender_phone = models.CharField(max_length=15)
    sender_address = models.CharField(max_length=255, default="Chittagong Road, Narayanganj")

    # Receiver Details
    receiver_name = models.CharField(max_length=255)
    receiver_phone = models.CharField(max_length=15)
    receiver_address = models.CharField(max_length=255)
    district = models.CharField(max_length=100)
    area = models.CharField(max_length=100, blank=True, null=True)

    # Delivery Details
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2)
    cod_option = models.BooleanField(default=False)
    cod_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cod_charge = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Payment and Pickup Details
    PAYMENT_OPTIONS = [
        ('cash', 'Cash'),
        ('to_pay', 'To Pay'),
    ]
    payment_option = models.CharField(
        max_length=10,
        choices=PAYMENT_OPTIONS,
        default='cash'
    )

    PICKUP_SYSTEM = [
        ('home_delivery', 'Home Delivery'),
        ('office_delivery', 'Office Delivery'),
    ]
    pickup_system = models.CharField(
        max_length=15,
        choices=PICKUP_SYSTEM,
        default='office_delivery'
    )

    # Date Details
    date_booked = models.DateField(auto_now_add=True)

    # Methods
    def calculate_cod_charge(self):
        """Calculate COD charge based on the COD amount."""
        if self.cod_option and self.cod_amount is not None:
            if 1 <= self.cod_amount <= 1000:
                self.cod_charge = 20
            elif 1001 <= self.cod_amount < 2000:
                self.cod_charge = 30
            elif 2001 <= self.cod_amount < 3000:
                self.cod_charge = 40
            elif 3001 <= self.cod_amount < 4000:
                self.cod_charge = 50
            elif 4001 <= self.cod_amount < 5000:
                self.cod_charge = 60
            elif 5001 <= self.cod_amount < 6000:
                self.cod_charge = 70
            elif 6001 <= self.cod_amount < 7000:
                self.cod_charge = 80
            elif 7001 <= self.cod_amount < 8000:
                self.cod_charge = 90
            elif 8001 <= self.cod_amount < 9000:
                self.cod_charge = 100
            elif 9001 <= self.cod_amount < 10000:
                self.cod_charge = 110
            elif 10001 <= self.cod_amount < 11000:
                self.cod_charge = 120
            elif 11001 <= self.cod_amount < 12000:
                self.cod_charge = 130
            elif 12001 <= self.cod_amount < 13000:
                self.cod_charge = 140
            elif 13001 <= self.cod_amount < 14000:
                self.cod_charge = 150
            elif 14001 <= self.cod_amount < 15000:
                self.cod_charge = 160
            elif 15001 <= self.cod_amount < 16000:
                self.cod_charge = 170
            else:
                # Optional: handle cod_amount > 16000 (if applicable)
                self.cod_charge = None  # or another appropriate value, like a custom rate or a message
            self.save()

    def __str__(self):
        return f"Parcel booked by {self.sender_name} for {self.receiver_name}"
