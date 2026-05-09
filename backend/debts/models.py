from django.db import models


class Debtor(models.Model):

    party_name = models.CharField(
        max_length=255
    )

    mobile_number = models.CharField(
        max_length=20
    )

    address = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.party_name


class Creditor(models.Model):

    party_name = models.CharField(
        max_length=255
    )

    mobile_number = models.CharField(
        max_length=20
    )

    address = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.party_name