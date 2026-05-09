from django.shortcuts import render, redirect

from .models import Stock


def stock_view(request):

    stocks = Stock.objects.all().order_by(
        '-id'
    )

    total_products = stocks.count()

    total_quantity = sum(
        item.quantity
        for item in stocks
    )

    context = {

        'stocks': stocks,

        'total_products': total_products,

        'total_quantity': total_quantity

    }

    return render(

        request,

        'stock/stock.html',

        context

    )

def save_stock(request):

    if request.method == 'POST':

        product_name = request.POST.get(
            'product_name'
        )

        quantity = request.POST.get(
            'quantity'
        )

        purchase_price = request.POST.get(
            'purchase_price'
        )

        selling_price = request.POST.get(
            'selling_price'
        )

        unit = request.POST.get(
            'unit'
        )

        total_amount = (
            float(quantity)
            *
            float(purchase_price)
        )

        Stock.objects.create(

            product_name=product_name,

            quantity=quantity,

            purchase_price=purchase_price,

            selling_price=selling_price,

            unit=unit,

            total_amount=total_amount

        )

    return redirect(
        '/dashboard/?page=stock'
    )