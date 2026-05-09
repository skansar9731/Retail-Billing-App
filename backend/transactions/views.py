from django.shortcuts import render


def purchase_view(request):

    return render(
        request,
        'transactions/purchase.html'
    )


def sales_view(request):

    return render(
        request,
        'transactions/sales.html'
    )

def dashboard_debtors(request):

    return render(
        request,
        'dashboard/dashboard.html',
        {
            'page': 'debtors'
        }
    )


def dashboard_creditors(request):

    return render(
        request,
        'dashboard/dashboard.html',
        {
            'page': 'creditors'
        }
    )