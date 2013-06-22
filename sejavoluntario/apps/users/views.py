from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sejavoluntario.apps.users.forms import AddressRegistrationForm
from sejavoluntario.apps.users.forms import BeneficiarioRegistrationForm
from sejavoluntario.apps.users.forms import BankDataRegistrationForm
from sejavoluntario.apps.users.forms import UserRegistrationForm

def userRegistration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'logged.html')
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
    import ipdb;ipdb.set_trace()
    if request.method == 'POST':
        form = AddressRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
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