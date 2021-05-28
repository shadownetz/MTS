from django.urls import path

from .views import *

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
    path('logout', signout, name='logout')
]
