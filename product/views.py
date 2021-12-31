from django.shortcuts import redirect, render

from product.models import Cart, ProductItem


def product(request):
    products = ProductItem.objects.all()

    context = {
        "products" : products,
    }

    return render(request, 'product.html', context=context)


def cart(request):
    cart_products = Cart.objects.all()

    context = {
        "cart_products" : cart_products
    }

    return render(request, 'cart.html', context=context)


def add_to_cart(request,pk):
    cart_product = ProductItem.objects.get(pk=pk)

    Cart.objects.create(
        product_name = cart_product.product_name, product_price = cart_product.product_price, product_image = cart_product.product_image
    )

    return redirect('/')


def remove(request,pk):
    remove_item = Cart.objects.get(pk=pk)

    remove_item.delete()

    return redirect('/cart')


def add_count(request,pk):
    add_count_product = Cart.objects.get(pk=pk)
    add_count_product.product_count += 1
    add_count_product.save()

    print("##################################################3###############################",add_count_product)

    return redirect('/cart')


def minus_count(request,pk):
    minus_count_product = Cart.objects.get(pk=pk)
    minus_count_product.product_count -= 1
    minus_count_product.save()

    print("##################################################3###############################",minus_count_product)

    return redirect('/cart')
