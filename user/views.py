from django.shortcuts import redirect, render
from django.contrib.auth import authenticate


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
    return render(request, 'signup.html')
