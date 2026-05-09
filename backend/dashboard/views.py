from django.shortcuts import render

from django.contrib.auth.decorators import (
    login_required
)

from debts.models import Debtor
from debts.models import Creditor

from stock.models import Stock

from invoices.models import Invoice


@login_required(login_url='/login/')
def dashboard_view(request):

    page = request.GET.get(
        'page',
        'dashboard'
    )

    debtors = Debtor.objects.all().order_by(
        '-id'
    )

    creditors = Creditor.objects.all().order_by(
        '-id'
    )

    stocks = Stock.objects.all().order_by(
        '-id'
    )

    purchase_invoices = Invoice.objects.filter(
        invoice_type='purchase'
    ).order_by('-id')

    sales_invoices = Invoice.objects.filter(
        invoice_type='sales'
    ).order_by('-id')

    total_products = stocks.count()

    total_quantity = sum(
        item.quantity
        for item in stocks
    )

    context = {

        'page': page,

        'debtors': debtors,

        'creditors': creditors,

        'stocks': stocks,

        'purchase_invoices':
            purchase_invoices,

        'sales_invoices':
            sales_invoices,

        'total_products':
            total_products,

        'total_quantity':
            total_quantity

    }

    return render(

        request,

        'dashboard/dashboard.html',

        context

    )