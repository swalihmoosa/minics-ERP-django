from json import dumps
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate

from user.form import CustomUserForm


def user_login(request):
    # authencation using session
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
    user_form = CustomUserForm(request.POST)

    if user_form.is_valid():
        user_form.save()

        response_data = {
            "status" : "success",
            "title" : "Successfully Added",
            "message" : "You added a new product"
        }
        return redirect('web:user_login')
    else:
        response_data = {
            "status" : "error",
            "title" : "An error Occured",
            "message" : "You can not add the product due to some Error"
        }

    dataJSON = dumps(response_data)
    context = {
        "form" : form,
        "response_data" : dataJSON
    }

    return render(request, 'signup.html', context=context)
