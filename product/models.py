from django.db import models


class ProductItem(models.Model):
    product_name = models.CharField(max_length=125)
    product_price = models.CharField(max_length=125)
    product_image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ["id"]


class Cart(models.Model):
    product_name = models.CharField(max_length=125)
    product_price = models.IntegerField()
    product_count = models.IntegerField(default=1)
    product_image = models.ImageField(upload_to="products/")
    product_total = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ["id"]





