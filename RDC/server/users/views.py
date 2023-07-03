from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from .models import Person
from django.contrib.auth import logout as userlogout, login as user_login, authenticate
from django.contrib.auth.decorators import login_required

def login(request, next="/"):
    if request.user.is_authenticated:
        return redirect("/")
    if request.POST:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            if user.is_active:
                user_login(request, user)
                return redirect(next)
        else:
            return render(request, "users/login.html")

    return render(request, "users/login.html")


def logout(request):
    userlogout(request)
    return redirect("/")