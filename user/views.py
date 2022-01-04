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

    context = {
        "form" : form
    }

    return render(request, 'signup.html', context=context)
