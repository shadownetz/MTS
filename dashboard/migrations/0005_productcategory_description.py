# Generated by Django 3.2.3 on 2021-05-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210525_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
