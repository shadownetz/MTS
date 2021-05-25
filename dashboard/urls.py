from django.urls import path
from .views import *

app_name = 'dashboard'

urlpatterns = [
    path('', index, name='index'),
    path('statistics', statistics, name='statistics'),
    path('logout', signout, name='logout')
]
