from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def user_login(request):
    # authencation using session
    # if request.method == 'POST':
    #     username = request.POST.get("username")
    #     password = request.POST.get("password")
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         request.session['username'] = username
    #         return redirect('/')

    # if "username" in request.session:
    #     return redirect('/')
    # return render(request, 'login.html')

    # authencation using django
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
            
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/')
