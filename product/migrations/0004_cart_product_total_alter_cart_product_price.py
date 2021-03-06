# Generated by Django 4.0 on 2021-12-31 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_cart_product_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_price',
            field=models.IntegerField(max_length=125),
        ),
    ]
