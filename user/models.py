from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=125)
    customer_job = models.CharField(max_length=125)
    customer_image = models.ImageField(upload_to="customer/")
    testimonial = models.ForeignKey('user.Testimonial', on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name

    class Meta:
        ordering = ["id"]


class Testimonial(models.Model):
    testimonial = models.TextField(max_length=255)

    def __str__(self):
        return self.testimonial

    class Meta:
        ordering = ["id"]