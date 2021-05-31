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
        for product in products:
            product_id = product['product_id']
            amount = float(product['amount'])
            quantity = int(product['quantity'])
            product = Product.objects.get(pk=product_id)
            product_purchase.purchases.create(
                product=product, amount=amount, quantity=quantity
            )
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
                'code': product.code,
                'image': product.image.url,
                'created_at': product.created_at,
                'updated_at': product.updated_at
            })
    return JsonResponse(data=response)
