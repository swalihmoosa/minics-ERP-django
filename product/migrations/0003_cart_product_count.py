# Generated by Django 4.0 on 2021-12-31 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_count',
            field=models.IntegerField(default=1),
        ),
    ]