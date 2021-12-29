from django.shortcuts import render

from product.models import ProductItem


def product(request):
    products = ProductItem.objects.all()

    context = {
        "products" : products
    }

    return render(request, 'product.html', context=context)


def cart(request):
    return render(request, 'cart.html')


