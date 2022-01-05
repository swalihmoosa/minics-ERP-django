import json

import os
from twilio.rest import Client

from django.core.mail import send_mail
from minics.settings import EMAIL_HOST_USER

from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate

from user.form import CustomUserForm
from user.models import CustomUser


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = CustomUser.objects.filter(username=username,password=password)
        if user:
            request.session['username'] = username
                        
            account_sid = 'ACba282cb048caedd49188eee2e085ad31'
            auth_token = '9ac7f23e3fd00fdce531f9b23f6a8fce'
            client = Client(account_sid, auth_token)
            message = client.messages \
                            .create(
                                body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                                from_='+12163501362',
                                to='+918129133008'
                            )

            print(message.sid)

            return redirect('web:index')
            

    if "username" in request.session:
        return redirect('web:index')
    return render(request, 'login.html')


def user_logout(request):
    del request.session['username']
    return redirect('web:user_login')


def user_signup(request):
    form = CustomUserForm()

    context = {
        "form" : form,
    }

    return render(request, 'signup.html', context=context)


def add_signup_user(request):
    form = CustomUserForm(request.POST)

    if form.is_valid():
        if not CustomUser.objects.filter(email=request.POST.get('email')).exists():
            if request.POST.get('password')==request.POST.get('confirm_password'):

                response_data = {
                    "status" : "success",
                    "title" : "Successfully Registered",
                    "message" : "You are successfully Created and Account"
                }

                subject = "MINICS WEBSITE"
                message = "You are successfully Created and Account"
                reciever = request.POST.get('email')
                send_mail(subject, message, EMAIL_HOST_USER, [reciever], fail_silently=False)
                form.save()

            else:
                response_data = {
                        "status" : "error",
                        "title" : "Password Error",
                        "message" : "Password Donot Match...! Check and try again"
                    }
        else:
            response_data = {
                "status" : "error",
                "title" : "You are Already Registered",
                "message" : "Email already exists..! try using another email"
            }
    else:
        response_data = {
            "status" : "error",
            "title" : "An error Occured",
            "message" : "You can not signup due to some Error"
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")