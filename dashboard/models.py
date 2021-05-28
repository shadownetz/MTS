from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


def product_image_upload_path(instance, filename):
    # file will be uploaded to media/products/images/product_name/<filename>
    return 'products/images/{0}/{1}'.format(instance.name, filename)


class ProductCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = _('product categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=50)
    image = models.ImageField(upload_to=product_image_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    discount = models.FloatField(default=0.0)
    amount = models.FloatField(default=0)
    total = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class ProductSale(models.Model):
    sales = models.ManyToManyField(Sale)
    paid_in_cash = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_sales(self):
        return ','.join(['{0}_{1}'.format(s.id, s.product.name) for s in self.sales.all()])


class ProductPurchase(models.Model):
    purchases = models.ManyToManyField(Purchase)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_purchases(self):
        return ','.join(['{0}_{1}'.format(s.id, s.product.name) for s in self.purchases.all()])


class CashFlow(models.Model):
    product_purchase = models.ForeignKey(ProductPurchase, on_delete=models.SET_NULL, null=True)
    product_sale = models.ForeignKey(ProductSale, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
