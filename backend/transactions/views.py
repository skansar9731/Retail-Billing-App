import random

from django.shortcuts import (
    render,
    redirect
)

from invoices.models import Invoice


# =========================
# PURCHASE
# =========================

def purchase_view(request):

    if request.method == 'POST':

        party_name = request.POST.get(
            'party_name',
            ''
        )

        product_name = request.POST.get(
            'product_name',
            ''
        )

        quantity = request.POST.get(
            'quantity',
            0
        )

        unit = request.POST.get(
            'unit',
            ''
        )

        purchase_price = request.POST.get(
            'purchase_price',
            0
        )

        total_amount = request.POST.get(
            'total_amount',
            0
        )

        # Generate Invoice Number

        invoice_number = (

            'PUR-'

            + str(

                random.randint(
                    10000,
                    99999
                )

            )

        )

        # Save Invoice

        Invoice.objects.create(

            invoice_type='purchase',

            party_name=party_name,

            product_name=product_name,

            quantity=quantity,

            unit=unit,

            purchase_price=purchase_price,

            total_amount=total_amount,

            invoice_number=invoice_number

        )

        return redirect(
            '/dashboard/?page=purchase-invoices'
        )

    return render(

        request,

        'transactions/purchase.html'

    )


# =========================
# SALES
# =========================

def sales_view(request):

    if request.method == 'POST':

        party_name = request.POST.get(
            'party_name',
            ''
        )

        product_name = request.POST.get(
            'product_name',
            ''
        )

        quantity = request.POST.get(
            'quantity',
            0
        )

        unit = request.POST.get(
            'unit',
            ''
        )

        purchase_price = request.POST.get(
            'purchase_price',
            0
        )

        selling_price = request.POST.get(
            'selling_price',
            0
        )

        total_amount = request.POST.get(
            'total_amount',
            0
        )

        net_profit = request.POST.get(
            'net_profit',
            0
        )

        # Generate Invoice Number

        invoice_number = (

            'SAL-'

            + str(

                random.randint(
                    10000,
                    99999
                )

            )

        )

        # Save Invoice

        Invoice.objects.create(

            invoice_type='sales',

            party_name=party_name,

            product_name=product_name,

            quantity=quantity,

            unit=unit,

            purchase_price=purchase_price,

            selling_price=selling_price,

            total_amount=total_amount,

            net_profit=net_profit,

            invoice_number=invoice_number

        )

        return redirect(
            '/dashboard/?page=sales-invoices'
        )

    return render(

        request,

        'transactions/sales.html'

    )