# coding: utf-8

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from sejavoluntario.apps.users.models import UserProfile
from sejavoluntario.apps.users.forms import LoginForm


def index(request):
    return render(request, "index.html")

def user_login(request):
    if request.user.is_authenticated():
        return render(request, "loggeduser.html")

    context = RequestContext(request)
    
    if request.method=="POST":
        import ipdb;ipdb.set_trace()
        form_login = LoginForm(request.POST)
        
        if request.POST.get('email') and request.POST.get('password'):
            email = request.POST.get('email')
            password = request.POST.get('password')

            usuario = User.objects.filter(Q(username=email))
            
            if not usuario:
                context.update({'form': form_login, 'messge': 'Usuário não está cadastrado'})
                return render(request, 'loginform.html', context)
            
            if usuario.is_active:
                if usuario.check_password(password):
                    login(request, usuario)
                    return render(request, 'logged.html', context)
                
                else:
                    form_login.errors.update( {'password': ['Senha inválida'] } )
            else:
                form_login.errors.update( {'email': ['Usuário inativo'] } )
            
    else:
        form_login = LoginForm()
      
    context.update({'form': form_login, 'remove_back_header': True, 'remove_cadastro_header': True})
    
    return render(request, 'loginform.html', context)
    
@login_required(login_url=settings.LOGIN_URL)
def logged_user(request):
    if request.user.is_authenticated():
        return render(request, "loggeduser.html")



