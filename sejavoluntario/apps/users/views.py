from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from sejavoluntario.apps.users.forms import AddressRegistrationForm
from sejavoluntario.apps.users.forms import BeneficiarioRegistrationForm
from sejavoluntario.apps.users.forms import BankDataRegistrationForm
from sejavoluntario.apps.users.forms import UserRegistrationForm
from sejavoluntario.apps.users.forms import UserUpdateForm
from sejavoluntario.apps.users.models import Beneficiario
from sejavoluntario.apps.users.models import Endereco
from sejavoluntario.apps.users.models import UserProfile
from sejavoluntario.apps.users.models import Voluntario

def userRegistration(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/me')
    else:
        form = UserRegistrationForm()

    return render(request, 'userregistrationform.html', {
        'form': form,
    })
    
def bankDataRegistration(request):
    if request.method == 'POST':
        form = BankDataRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
    else:
        form = BankDataRegistrationForm()

    return render(request, 'bankdataregistrationform.html', {
        'form': form,
    })

@login_required(login_url=settings.LOGIN_URL)
def addressRegistration(request):
    if request.method == 'POST':
        form = AddressRegistrationForm(request.POST)
        if form.is_valid():
            if not request.POST.get("endereco_id"):
                endereco = form.save()
                usuario_id = request.POST.get("usuario_id")
                usuario = Voluntario.objects.get(id=usuario_id)
                usuario.endereco = endereco
                usuario.save()
            else:
                endereco = Endereco.objects.get(id=request.POST.get("endereco_id"))
                endereco.logradouro = request.POST.get("logradouro")
                endereco.numero = request.POST.get("numero")
                endereco.cep = request.POST.get("cep")
                endereco.complemento = request.POST.get("complemento")
                
                endereco.save()
                
            
            return redirect('/me')
    else:
        form = AddressRegistrationForm()

    return render(request, 'addressregistrationform.html', {
        'form': form,
    })
    
def beneficiarioRegistration(request):
    if request.method == 'POST':
        form = BeneficiarioRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
    else:
        form = BeneficiarioRegistrationForm()

    return render(request, 'beneficiarioregistrationform.html', {
        'form': form,
    })
    
@login_required(login_url=settings.LOGIN_URL)
def user_profile(request):
    
    voluntario = Voluntario.objects.get(user=request.user.id)
    endereco = voluntario.endereco
    
    if endereco:
        address_data = {
                        'logradouro' : endereco.logradouro,
                        'cep' : endereco.cep,
                        'numero' : endereco.numero,
                        'complemento' : endereco.complemento,
                        'bairro' : endereco.bairro,
                        }
    else:
        address_data = {}

    if voluntario:
        volunteer_data ={
                         'username':voluntario.user.username,
                         'first_name':voluntario.user.first_name,
                         'last_name':voluntario.user.last_name,
                         'email':voluntario.user.email,
                         'password':'',
                         'repeat_password':'',
                         }
    else:
        volunteer_data = {}
    
    #if request.POST.get('endereco_id'):
    address_form = AddressRegistrationForm(address_data)
    volunteer_form = UserUpdateForm(volunteer_data)

    return render(request, 'profile.html', {
        'address_form': address_form,
        'volunteer_form':volunteer_form,
        'endereco':endereco,
        'usuario':voluntario,
    })

@login_required(login_url=settings.LOGIN_URL)
def change_password(request):
    if request.GET:
        return redirect("/me")
    
    password = request.POST.get('password')
    repeat_password = request.POST.get('repeat_password')
    
    if not password and not repeat_password:
        return redirect("/me")
    
    if password == repeat_password:
        user = User.objects.get(id=request.user.id)
        user.set_password(password)
        user.save()
        
    return redirect("/me")
    
def show_beneficiario(request, beneficiario_id):
    beneficiario = get_object_or_404(Beneficiario, id=beneficiario_id)

    return render(request, 'beneficiario.html',
               {
                'beneficiario':beneficiario,
                }
               )