from django.db import models


class ProductItem(models.Model):
    product_name = models.CharField(max_length=125)
    product_price = models.CharField(max_length=125)
    product_image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ["id"]





