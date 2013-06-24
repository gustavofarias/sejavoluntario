# coding: utf-8

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.template import RequestContext
from django.utils import simplejson

import json

from sejavoluntario.apps.users.forms import LoginForm
from sejavoluntario.apps.users.models import Area
from sejavoluntario.apps.users.models import Beneficiario
from sejavoluntario.apps.users.models import UserProfile
from sejavoluntario.apps.users.models import Voluntario

def index(request):
    return render(request, "index.html")

def user_login(request):
    if request.user.is_authenticated():
        return redirect("/me")

    context = RequestContext(request)
    
    if request.method=="POST":
        form_login = LoginForm(request.POST)
        
        if request.POST.get('email') and request.POST.get('password'):
            email = request.POST.get('email')
            password = request.POST.get('password')

            usuario = User.objects.filter(Q(username=email))
            
            if not usuario:
                context.update({'form': form_login, 'message': 'Usuário não está cadastrado'})
                return render(request, 'loginform.html', context)
            
            usuario = usuario[0]
            import ipdb;ipdb.set_trace()
            usuario = authenticate(username=usuario.email, password=password)
            if usuario.is_active:
                if usuario.check_password(password):
                    login(request, usuario)
                    return render(request, 'loggeduser.html', context)
                
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
    
    if not request.user.is_authenticated():
        return redirect("/user/logout")
    
    usuario = UserProfile.objects.get(user=request.user)
    
    if not usuario:
        return redirect("/user/logout")
    
    context = RequestContext(request)
    try:
        voluntario = usuario.voluntario
        beneficiario = None
        areas = voluntario.areas.all()[0]
        context.update({'voluntario': voluntario, 'areas':areas})
    except:
        beneficiario = usuario.beneficiario
        voluntario = None
        areas = beneficiario.areas.all()[0]
        context.update({'beneficiario': beneficiario, 'areas':areas})
    
    
    return render(request, "loggeduser.html", context)
    
def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
    
    form_login = LoginForm()

    context = RequestContext(request)
    context.update({'form': form_login, 'remove_back_header': True, 'remove_cadastro_header': True})
    
    return render(request, 'loginform.html', context)

def lista_beneficiarios(request, area=None, bairro=None, qtd=None):
    area = Area.objects.filter(name=area)

    if area:
        if bairro:
            listagem_beneficiarios = Beneficiario.objects.filter(areas=area, endereco__bairro=bairro)[:qtd]
        else:
            listagem_beneficiarios = Beneficiario.objects.filter(areas=area)[:qtd]
            
    else:
        return redirect("/me")
            
    json_beneficiarios = {}
    for beneficiario in listagem_beneficiarios:
        json_beneficiarios[beneficiario.user.first_name] = beneficiario.user.first_name

    return HttpResponse(json.dumps(json_beneficiarios), content_type="application/json")