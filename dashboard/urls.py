from django.urls import path
from .views import *

app_name = 'dashboard'

urlpatterns = [
    path('', index, name='index'),
    path('statistics', statistics, name='statistics'),
    path('categories',  categories, name='categories'),
    path('categories/delete', delete_category, name='delete_category'),
    path('logout', signout, name='logout')
]
