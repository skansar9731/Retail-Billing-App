from django.urls import path

from .views import *

urlpatterns = [

    path(
        'save-debtor/',
        save_debtor
    ),

    path(
        'delete-debtor/<int:id>/',
        delete_debtor
    ),

    path(
        'save-creditor/',
        save_creditor
    ),

    path(
        'delete-creditor/<int:id>/',
        delete_creditor
    ),

path(
    'edit-debtor/<int:id>/',
    edit_debtor
),

path(
    'edit-creditor/<int:id>/',
    edit_creditor
),
]