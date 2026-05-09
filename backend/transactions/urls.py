from django.urls import path

from . import views


urlpatterns = [

    path(
        'purchase/',
        views.purchase_view,
        name='purchase'
    ),

    path(
        'sales/',
        views.sales_view,
        name='sales'
    ),

]