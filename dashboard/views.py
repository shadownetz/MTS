from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import *
from home.models import User
from .forms import (AddProductForm, PurchaseForm, UserAvatarForm, UserProfileForm, UserPasswordForm)
# from functools import reduce


@login_required
def index(request):
    all_category = ProductCategory.objects.all()
    return render(request, 'dashboard/dashboard.html', {
        'categories': all_category
    })


@login_required
def statistics(request):
    cash_flows = CashFlow.objects.all().order_by('-created_at')
    purchases_count = 0
    sales_count = 0
    for flow in cash_flows:
        if flow.product_purchase:
            purchases_count += flow.product_purchase_amount
        if flow.product_sale:
            sales_count += flow.product_sale_amount
    stats = {
        'purchases': purchases_count,
        'products': Product.objects.count(),
        'users': User.objects.count(),
        'sales': {
            'count': sales_count,
            'profit': sales_count > purchases_count,
            'profit_level': (sales_count-purchases_count) % 100
        },
        'cashFlows': cash_flows
    }
    print((sales_count-purchases_count) % 100)
    return render(request, 'dashboard/statistics.html', stats)


@login_required
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
    all_categories = ProductCategory.objects.all().order_by('-created_at')
    return render(request, 'dashboard/categories.html', {
        'categories': all_categories
    })


@login_required
def delete_category(request):
    try:
        ProductCategory.objects.get(pk=request.GET.get('id')).delete()
    except KeyError:
        pass
    return redirect('dashboard:categories')


@login_required
def products(request):
    all_products = Product.objects.all().order_by('-created_at')
    return render(request, 'dashboard/products/productList.html', {
        'products': all_products
    })


@login_required
def product_add(request):
    product_form = AddProductForm()
    if request.method == 'POST':
        product_form = AddProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('dashboard:products')
    return render(request, 'dashboard/products/productAdd.html', {
        'productForm': product_form
    })


@login_required
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


@login_required
def product_delete(request):
    try:
        Product.objects.get(pk=request.GET.get('id')).delete()
    except (KeyError, Product.DoesNotExist):
        pass
    return redirect('dashboard:products')


@login_required
def purchases(request):
    all_purchases = ProductPurchase.objects.all().order_by('-created_at')
    return render(request, 'dashboard/purchase/purchaseList.html', {
        'purchases': all_purchases
    })


@login_required
def add_purchases(request):
    all_products = Product.objects.all()
    return render(request, 'dashboard/purchase/purchaseAdd.html', {
        'products': all_products
    })


@login_required
def edit_purchase(request, purchase_id):

    try:
        purchase = Purchase.objects.get(pk=purchase_id)
        purchase_form = PurchaseForm(instance=purchase)
        if request.method == 'POST':
            purchase_form = PurchaseForm(request.POST, instance=purchase)
            if purchase_form.is_valid():
                purchase_form.save()
        else:
            return render(request, 'dashboard/purchase/purchaseEdit.html', {
                'purchaseForm': purchase_form
            })
    except Purchase.DoesNotExist:
        pass
    return redirect('dashboard:purchases')


@login_required
def purchase_delete(request):
    try:
        product_purchase = ProductPurchase.objects.get(pk=request.GET.get('pur_id'))
        purchase = Purchase.objects.get(pk=request.GET.get('id'))
        product_purchase.purchases.remove(purchase)
    except (KeyError, Purchase.DoesNotExist, ProductPurchase.DoesNotExist):
        pass
    return redirect('dashboard:purchases')


@login_required
def sales(request):
    all_sales = ProductSale.objects.all().order_by('-created_at')
    return render(request, 'dashboard/sale/saleList.html', {
        'sales': all_sales
    })


@login_required
def sales_delete(request):
    try:
        products_sale = ProductSale.objects.get(pk=request.GET.get('pro_id'))
        sale = Sale.objects.get(pk=request.GET.get('id'))
        products_sale.sales.remove(sale)
    except (KeyError, ProductSale.DoesNotExist, Sale.DoesNotExist):
        pass
    return redirect('dashboard:sales')


@login_required
def staffs(request):
    all_users = User.objects.all().order_by('-created_at')
    return render(request, 'dashboard/user/users.html', {
        'users': all_users
    })


@login_required
def staff_manage(request):
    user_id = request.GET.get('id')
    action = request.GET.get('action')
    if action == '0':
        try:
            user = User.objects.get(pk=user_id)
            user.is_active = not user.is_active
            user.save()
        except User.DoesNotExist:
            pass
    elif action == '1':
        try:
            User.objects.get(pk=user_id).delete()
        except User.DoesNotExist:
            pass
    return redirect('dashboard:staffs')


@login_required
def cash_flows(request):
    _cash_flows = CashFlow.objects.all().order_by('-created_at')
    return render(request, 'dashboard/cashFlow.html', {
        'cashFlows': _cash_flows
    })


@login_required
def user_profile(request):
    avatar_form = UserAvatarForm()
    profile_form = UserProfileForm(instance=request.user)
    password_form = UserPasswordForm()
    return render(request, 'dashboard/user/userProfile.html', {
        'avatar_form': avatar_form,
        'profile_form': profile_form,
        'password_form': password_form
    })


@login_required
def update_user_avatar(request):
    if request.method == 'POST':
        avatar_form = UserAvatarForm(request.POST, request.FILES, instance=request.user)
        if avatar_form.is_valid():
            avatar_form.save()
    return redirect('dashboard:profile')


@login_required
def update_user_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
        else:
            avatar_form = UserAvatarForm()
            password_form = UserPasswordForm()
            return render(request, 'dashboard/user/userProfile.html', {
                'avatar_form': avatar_form,
                'profile_form': profile_form,
                'password_form': password_form
            })
    return redirect('dashboard:profile')


@login_required
def update_user_password(request):
    if request.method == 'POST':
        password_form = UserPasswordForm(request.POST)
        if password_form.is_valid():
            new_password = password_form.cleaned_data['password']
            user = User.objects.get(pk=request.user.id)
            user.set_password(new_password)
            user.save()
        else:
            avatar_form = UserAvatarForm()
            profile_form = UserProfileForm(instance=request.user)
            return render(request, 'dashboard/user/userProfile.html', {
                'avatar_form': avatar_form,
                'profile_form': profile_form,
                'password_form': password_form
            })
    return redirect('dashboard:profile')


def signout(request):
    logout(request)
    return redirect('login')
