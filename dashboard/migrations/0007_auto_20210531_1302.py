# Generated by Django 3.2.3 on 2021-05-31 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20210531_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashflow',
            name='product_purchase_amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='cashflow',
            name='product_sale_amount',
            field=models.FloatField(default=0.0),
        ),
    ]
