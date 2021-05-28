from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = (
        'id', 'name', 'category', 'code', 'image', 'created_at',
        'updated_at'
    )

    fieldsets = (
        (None, {
            'fields': (
                'name', 'category', 'code', 'image',
            )
        }),
    )

    ordering = ('id', 'created_at')


class SaleAdmin(admin.ModelAdmin):
    model = Sale
    list_display = (
        'id', 'product', 'quantity', 'discount', 'amount', 'total',
        'created_at', 'updated_at'
    )

    fieldsets = (
        (None, {
            'fields': (
                'product', 'quantity', 'discount', 'amount', 'total',
            )
        }),
    )

    ordering = ('id', 'created_at')


class PurchaseAdmin(admin.ModelAdmin):
    model = Purchase
    list_display = (
        'id', 'product', 'amount', 'quantity',
        'created_at', 'updated_at'
    )

    fieldsets = (
        (None, {
            'fields': (
                'product', 'amount', 'quantity',
            )
        }),
    )

    ordering = ('id', 'created_at')


class ProductSaleAdmin(admin.ModelAdmin):
    model = ProductSale
    list_display = (
        'id', 'get_sales', 'paid_in_cash', 'created_by',
        'created_at', 'updated_at'
    )

    fieldsets = (
        (None, {
            'fields': (
                'sales', 'paid_in_cash', 'created_by',
            )
        }),
    )

    ordering = ('id', 'created_at')


class ProductPurchaseAdmin(admin.ModelAdmin):
    model = ProductPurchase
    list_display = (
        'id', 'get_purchases', 'created_by',
        'created_at', 'updated_at'
    )

    fieldsets = (
        (None, {
            'fields': (
                'purchases', 'created_by',
            )
        }),
    )

    ordering = ('id', 'created_at')


class CashFlowAdmin(admin.ModelAdmin):
    model = CashFlow
    list_display = (
        'id', 'product_purchase', 'product_sale',
        'created_at'
    )

    fieldsets = (
        (None, {
            'fields': (
                'product_purchase', 'product_sale',
            )
        }),
    )

    ordering = ('id', 'created_at')


class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory
    list_display = (
        'id', 'name', 'description', 'created_at'
    )

    fieldsets = (
        (None, {
            'fields': (
                'name', 'description'
            )
        }),
    )

    ordering = ('id', 'created_at')


admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(ProductSale, ProductSaleAdmin)
admin.site.register(ProductPurchase, ProductPurchaseAdmin)
admin.site.register(CashFlow, CashFlowAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
