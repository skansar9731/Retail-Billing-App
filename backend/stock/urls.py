from django.urls import path

from .views import stock_view, save_stock


urlpatterns = [

    path(
        '',
        stock_view,
        name='stock'
    ),
path(
    'save/',
    save_stock,
    name='save_stock'
),

]