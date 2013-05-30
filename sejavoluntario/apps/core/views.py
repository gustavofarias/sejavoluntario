from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def loggedUser(request):
    return render(request, "loggeduser.html")