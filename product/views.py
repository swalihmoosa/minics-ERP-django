from django.shortcuts import redirect, render

from product.models import Cart, ProductItem


def product(request):
    if "username" in request.session:
        products = ProductItem.objects.all()

        context = {
            "products" : products,
        }

        return render(request, 'product.html', context=context)
    else:
        return redirect('web:user_login')


def cart(request):
    if "username" in request.session:
        cart_products = Cart.objects.all()
        sub_total = 0 
        taxes = sub_total * 6/100
        shipping = sub_total * 2/100
        grant_total = sub_total + taxes + shipping

        for cart_product in cart_products:
            cart_product.product_total = cart_product.product_price * cart_product.product_count 
            cart_product.save()

            sub_total += cart_product.product_total
            taxes = sub_total * 6/100
            shipping = sub_total * 2/100
            grant_total = sub_total + taxes + shipping

        context = {
            "cart_products" : cart_products,
            "sub_total" : sub_total,
            "taxes" : taxes,
            "shipping" : shipping,
            "grant_total" : grant_total,
        }

        return render(request, 'cart.html', context=context)
    else:
        return redirect('web:user_login')


def add_to_cart(request,pk):
    cart_product = ProductItem.objects.get(pk=pk)

    if not Cart.objects.filter(product_name=cart_product.product_name).exists():
        Cart.objects.create(
            product_name = cart_product.product_name, product_price = cart_product.product_price, product_image = cart_product.product_image
        )
    else:
        cart_product = Cart.objects.get(product_name=cart_product.product_name)
        cart_product.product_count +=1
        cart_product.save()
    return redirect('web:index')


def remove(request,pk):
    remove_item = Cart.objects.get(pk=pk)

    remove_item.delete()

    return redirect('web:cart')


def add_count(request,pk):
    add_count_product = Cart.objects.get(pk=pk)
    add_count_product.product_count += 1
    add_count_product.save()

    return redirect('web:cart')


def minus_count(request,pk):
    minus_count_product = Cart.objects.get(pk=pk)
    minus_count_product.product_count -= 1
    minus_count_product.save()

    return redirect('web:cart')
