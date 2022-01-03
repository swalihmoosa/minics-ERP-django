from django.shortcuts import redirect, render
from django.contrib.auth import authenticate


def user_login(request):
    # authencation using session
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        keep_signin = request.POST.get("keep_signin")
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            if keep_signin == "on":
                SESSION_EXPIRE_SECONDS = 60
            return redirect('web:index')
            

    if "username" in request.session:
        return redirect('web:index')
    return render(request, 'login.html')


def user_logout(request):
    request.session.flush()
    return redirect('web:user_login')
