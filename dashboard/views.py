from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import AddProductForm


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
        except (ProductCategory.DoesNotExist, IntegrityError, KeyError):
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


def products(request):
    all_products = Product.objects.all()
    return render(request, 'dashboard/products/productList.html', {
        'products': all_products
    })


def product_add(request):
    product_form = AddProductForm()
    if request.method == 'POST':
        new_product = AddProductForm(request.POST, request.FILES)
        if new_product.is_valid():
            new_product.save()
            return redirect('dashboard:products')
    return render(request, 'dashboard/products/productAdd.html', {
        'productForm': product_form
    })


def product_edit(request, product_id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(pk=product_id)
            product_form = AddProductForm(request.POST, request.FILES, instance=product)
            if product_form.is_valid():
                product_form.save()
                return redirect('dashboard:products')
        except Product.DoesNotExist:
            return redirect('dashboard:products')
    try:
        product = Product.objects.get(pk=product_id)
        product_form = AddProductForm(instance=product)
        return render(request, 'dashboard/products/productEdit.html', {
            'productForm': product_form
        })
    except Product.DoesNotExist:
        return redirect('dashboard:products')


def product_delete(request):
    try:
        Product.objects.get(pk=request.GET.get('id')).delete()
    except (KeyError, Product.DoesNotExist):
        pass
    return redirect('dashboard:products')


def signout(request):
    logout(request)
    return redirect('login')
