# coding: utf-8

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def user_login(request):
    if request.user.is_authenticated():
        return render(request, "loggeduser.html")

@login_required(login_url=settings.LOGIN_URL)
def logged_user(request):
    if request.user.is_authenticated():
        return render(request, "loggeduser.html")



