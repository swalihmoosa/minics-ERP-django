import json

from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from minics.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from product.models import ProductItem
from user.models import Customer
from web.forms import SubscribeForm
from web.models import Subscribe

def index(request):
    if "username" in request.session:
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
    else:
        return redirect('web:user_login')


def about(request):
    if "username" in request.session:
        return render(request, 'about.html')
    return redirect('web:user_login')


def why(request):
    if "username" in request.session:
        return render(request, 'why.html')
    return redirect('web:user_login')


def testimonial(request):
    if "username" in request.session:
        customers = Customer.objects.all()

        context = {
            "customers" : customers
        }

        return render(request, 'testimonial.html', context=context)
    return redirect('web:user_login')


def subscribe(request):
    if "username" in request.session:
        subscribe_form = SubscribeForm(request.POST)

        if subscribe_form.is_valid():
            if not Subscribe.objects.filter(email=request.POST.get('email')).exists():
                subscribe_form.save()

                response_data = {
                    "status" : "success",
                    "title" : "Successfully Registered",
                    "message" : "You are Subscribed to the News Letter"
                }
                
                subject = "MINICS WEBSITE"
                message = "You are Subscribed to the News Letter"
                reciever = request.POST.get('email')
                send_mail(subject, message, EMAIL_HOST_USER, [reciever], fail_silently=False)
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
    return redirect('web:user_login')