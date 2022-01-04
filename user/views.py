import json
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
        print("################################################################",user)
        if user:
            request.session['username'] = username
            return redirect('web:index')
            

    if "username" in request.session:
        return redirect('web:index')
    return render(request, 'login.html')


def user_logout(request):
    request.session.flush()
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
                form.save()

                response_data = {
                    "status" : "success",
                    "title" : "Successfully Registered",
                    "message" : "You are successfully Created and Account"
                }
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