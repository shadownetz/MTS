from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# @login_required
def index(request):
    return render(request, 'dashboard/dashboard.html')


def statistics(request):
    return render(request, 'dashboard/base.html')


def signout(request):
    logout(request)
    return redirect('login')
