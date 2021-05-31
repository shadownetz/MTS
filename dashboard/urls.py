from django.urls import path

from .views import *
from .apis import (add_purchase, get_products, add_sale)

app_name = 'dashboard'

urlpatterns = [
    path('', index, name='index'),
    path('statistics', statistics, name='statistics'),
    path('categories',  categories, name='categories'),
    path('categories/delete', delete_category, name='delete_category'),
    path('products', products, name='products'),
    path('products/add', product_add, name='products_add'),
    path('products/update/<int:product_id>', product_edit, name='products_edit'),
    path('products/delete', product_delete, name='products_delete'),

    path('purchases', purchases, name='purchases'),
    path('purchases/add', add_purchases, name='purchases_add'),
    path('purchases/update/<int:purchase_id>', edit_purchase, name='purchases_edit'),
    path('purchases/delete', purchase_delete, name='purchases_delete'),

    path('sales', sales, name='sales'),
    path('sales/delete', sales_delete, name='sales_delete'),

    path('logout', signout, name='logout'),

    path('api/purchase/add', add_purchase, name='api_purchase_add'),
    path('api/products/fetch', get_products, name='api_products_fetch'),

    path('api/sale/add', add_sale, name='api_sale_add'),
]
