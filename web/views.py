from django.shortcuts import render

from product.models import ProductItem
from user.models import Customer


def index(request):
    products = ProductItem.objects.all()
    customers = Customer.objects.all()

    context = {
        "products" : products,
        "customers" : customers
    }
    
    return render(request, 'index.html', context=context)