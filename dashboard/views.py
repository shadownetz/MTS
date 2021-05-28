from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import ProductCategory


# @login_required
def index(request):
    return render(request, 'dashboard/dashboard.html')


def statistics(request):
    return render(request, 'dashboard/statistics.html')


def categories(request):
    if request.method == 'POST':
        try:
            product_category = ProductCategory.objects.get(pk=request.POST['edit_id'])
            product_category.name = request.POST['name']
            product_category.description = request.POST['description']
            product_category.save()
        except (ProductCategory.DoesNotExist, IntegrityError):
            ProductCategory.objects.create(
                name=request.POST['name'], description=request.POST['description']
            )
    all_categories = ProductCategory.objects.all()
    return render(request, 'dashboard/categories.html', {
        'categories': all_categories
    })


def delete_category(request):
    try:
        ProductCategory.objects.get(pk=request.GET.get('id')).delete()
    except KeyError:
        pass
    return redirect('dashboard:categories')


def signout(request):
    logout(request)
    return redirect('login')
