from django.shortcuts import render

from django.contrib.auth.decorators import (
    login_required
)
from debts.models import (
    Debtor,
    Creditor
)


@login_required(login_url='/login/')
def dashboard_view(request):

    page = request.GET.get(
        'page',
        'dashboard'
    )

    context = {

        'page': page,
        'debtors': Debtor.objects.all(),

    'creditors': Creditor.objects.all(),

    }

    return render(

        request,

        'dashboard/dashboard.html',

        context

    )