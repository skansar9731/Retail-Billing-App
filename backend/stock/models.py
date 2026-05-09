from django.db import models


class Stock(models.Model):

    product_name = models.CharField(
        max_length=255
    )

    unit = models.CharField(
        max_length=50
    )

    quantity = models.IntegerField(
        default=0
    )

    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.product_name