# Generated by Django 3.2.3 on 2021-05-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210523_2305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'product categories'},
        ),
        migrations.AddField(
            model_name='productsale',
            name='paid_in_cash',
            field=models.BooleanField(default=True),
        ),
    ]
