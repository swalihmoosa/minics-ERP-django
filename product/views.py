from django.shortcuts import render

from product.models import ProductItem


def product(request):
    products = ProductItem.objects.all()

    context = {
        "products" : products
    }

    return render(request, 'product.html', context=context)


