import json

from django.http.response import HttpResponse
from django.shortcuts import render

from product.models import ProductItem
from user.models import Customer
from web.forms import SubscribeForm
from web.models import Subscribe


def index(request):
    products = ProductItem.objects.all()
    customers = Customer.objects.all()
    carousel_products = ProductItem.objects.all()[:1]
    carousel_customers = Customer.objects.all()[:1]
    subscribe_form = SubscribeForm()

    context = {
        "products" : products,
        "customers" : customers,
        "carousel_products" : carousel_products,
        "carousel_customers" : carousel_customers,
        "subscribe_form" : subscribe_form
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


def subscribe(request):
    subscribe_form = SubscribeForm(request.POST)

    if subscribe_form.is_valid():
        if not Subscribe.objects.filter(email=request.POST.get('email')).exists():
            subscribe_form.save()

            response_data = {
                "status" : "success",
                "title" : "Successfully Registered",
                "message" : "You are Subscribed to the News Letter"
            }
        else:
            response_data = {
                "status" : "error",
                "title" : "Already Registered",
                "message" : "You are Already Subscribed to the News Letter,no need to Subscribe again"
            }
    else:
        response_data = {
                "status" : "error",
                "title" : "Your Form is Not Valid",
                "message" : "Your Form is Not Valid,Try again"
    }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")