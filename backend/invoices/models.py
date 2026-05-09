from django.db import models


class Invoice(models.Model):

    INVOICE_TYPES = (

        ('purchase', 'Purchase'),

        ('sales', 'Sales'),

        ('purchase_return', 'Purchase Return'),

        ('sales_return', 'Sales Return'),

    )

    invoice_type = models.CharField(
        max_length=30,
        choices=INVOICE_TYPES
    )

    party_name = models.CharField(
        max_length=255
    )

    product_name = models.CharField(
        max_length=255
    )

    quantity = models.IntegerField()

    unit = models.CharField(
        max_length=50
    )

    purchase_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    selling_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    net_profit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    invoice_number = models.CharField(
        max_length=100,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.invoice_number