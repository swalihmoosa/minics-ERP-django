from django.shortcuts import redirect, render

from product.models import Cart, ProductItem


def product(request):
    products = ProductItem.objects.all()

    context = {
        "products" : products
    }

    return render(request, 'product.html', context=context)


def cart(request):
    return render(request, 'cart.html')


def add_to_cart(request,pk):
    cart_product = ProductItem.objects.get(pk=pk)

    print("###############################################****************************************",cart_product)


    return render(request, 'cart.html')

