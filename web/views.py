from django.shortcuts import render

from product.models import ProductItem
from user.models import Customer


def index(request):
    products = ProductItem.objects.all()
    customers = Customer.objects.all()
    carousel_products = ProductItem.objects.all()[:1]

    context = {
        "products" : products,
        "customers" : customers,
        "carousel_products" : carousel_products
    }
    
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html')


def why(request):
    return render(request, 'why.html')


def testimonial(request):
    customers = Customer.objects.all()

    context = {
        "customers" : customers
    }
    return render(request, 'testimonial.html', context=context)