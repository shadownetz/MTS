from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_index, name='home'),
    path('signup', register, name='register'),
    path('login', mts_login, name='login'),
    path('dashboard/', include('dashboard.urls'))
]
