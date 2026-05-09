from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import (
    Debtor,
    Creditor
)


# =========================
# DEBTORS
# =========================

def save_debtor(request):

    if request.method == 'POST':

        Debtor.objects.create(

            party_name=request.POST.get(
                'party_name'
            ),

            mobile_number=request.POST.get(
                'mobile_number'
            ),

            address=request.POST.get(
                'address'
            )

        )

    return redirect(
        '/dashboard/?page=debtors'
    )


def delete_debtor(request, id):

    debtor = get_object_or_404(
        Debtor,
        id=id
    )

    debtor.delete()

    return redirect(
        '/dashboard/?page=debtors'
    )


# =========================
# CREDITORS
# =========================

def save_creditor(request):

    if request.method == 'POST':

        Creditor.objects.create(

            party_name=request.POST.get(
                'party_name'
            ),

            mobile_number=request.POST.get(
                'mobile_number'
            ),

            address=request.POST.get(
                'address'
            )

        )

    return redirect(
        '/dashboard/?page=creditors'
    )


def delete_creditor(request, id):

    creditor = get_object_or_404(
        Creditor,
        id=id
    )

    creditor.delete()

    return redirect(
        '/dashboard/?page=creditors'
    )

# =========================
# UPDATE DEBTOR
# =========================

def edit_debtor(request, id):

    debtor = get_object_or_404(
        Debtor,
        id=id
    )

    if request.method == 'POST':

        debtor.party_name = request.POST.get(
            'party_name'
        )

        debtor.mobile_number = request.POST.get(
            'mobile_number'
        )

        debtor.address = request.POST.get(
            'address'
        )

        debtor.save()

        return redirect(
            '/dashboard/?page=debtors'
        )


# =========================
# UPDATE CREDITOR
# =========================

def edit_creditor(request, id):

    creditor = get_object_or_404(
        Creditor,
        id=id
    )

    if request.method == 'POST':

        creditor.party_name = request.POST.get(
            'party_name'
        )

        creditor.mobile_number = request.POST.get(
            'mobile_number'
        )

        creditor.address = request.POST.get(
            'address'
        )

        creditor.save()

        return redirect(
            '/dashboard/?page=creditors'
        )