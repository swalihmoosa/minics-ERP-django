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


def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')

def why(request):
    return render(request, 'why.html')

def testimonial(request):
    return render(request, 'testimonial.html')