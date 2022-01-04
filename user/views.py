import json
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate

from user.form import CustomUserForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
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
        form.save()

        response_data = {
            "status" : "success",
            "title" : "Successfully Registered",
            "message" : "You are successfully Created and Account"
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "An error Occured",
            "message" : "You can not signup due to some Error"
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")