from django.http import JsonResponse
from .models import *
from home.models import User
import json


def add_purchase(request):
    response = {
        'status': False
    }
    if request.method == 'POST':
        products = json.loads(request.POST['purchases'])
        user_id = request.POST['user_id']
        user = User.objects.get(pk=user_id)
        product_purchase = ProductPurchase(created_by=user)
        product_purchase.save()
        cash_flow = CashFlow(product_purchase=product_purchase)
        for product in products:
            product_id = product['product_id']
            amount = float(product['amount'])
            quantity = int(product['quantity'])
            _product = Product.objects.get(pk=product_id)
            product_purchase.purchases.create(
                product=_product, amount=amount, quantity=quantity
            )
            cash_flow.product_purchase_amount += amount*quantity
        cash_flow.save()
        response['status'] = True
    return JsonResponse(data=response)


def add_sale(request):
    response = {
        'status': False
    }
    if request.method == 'POST':
        sales = json.loads(request.POST['sales'])
        user_id = request.POST['user_id']
        user = User.objects.get(pk=user_id)
        product_sale = ProductSale(
            created_by=user,
            paid_in_cash=True if request.POST['paid_in_cash'] == 'true' else False
        )
        product_sale.save()
        cash_flow = CashFlow(product_sale=product_sale)
        for sale in sales:
            product_id = sale['product_id']
            amount = float(sale['amount'])
            quantity = int(sale['quantity'])
            discount = float(sale['discount'])
            total = (amount-((discount/100)*amount)) * quantity
            product = Product.objects.get(pk=product_id)

            product_sale.sales.create(
                product=product, amount=amount, quantity=quantity,
                discount=discount, total=total
            )
            cash_flow.product_sale_amount += total
        cash_flow.save()
        response['status'] = True
    return JsonResponse(data=response)


def get_products(request):
    response = {
        'status': True,
        'products': []
    }
    if request.method == 'GET':
        all_products = Product.objects.all()
        for product in all_products:
            response['products'].append({
                'id': product.id,
                'name': product.name,
                'category': product.category.name,
                'category_id': product.category.id,
                'code': product.code,
                'quantity': product.quantity,
                'image': product.image.url,
                'created_at': product.created_at,
                'updated_at': product.updated_at
            })
    return JsonResponse(data=response)


def get_admins(request):
    response = {'status': True, 'data': []}
    if request.method == 'GET':
        admins = User.objects.filter(is_staff=True)
        for admin in admins:
            response['data'].append({
                'name': admin.name,
                'phone': admin.phone
            })
    return JsonResponse(data=response)
