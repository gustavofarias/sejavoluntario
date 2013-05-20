from django.shortcuts import render
from sejavoluntario.apps.users.forms import AddressRegistrationForm
from sejavoluntario.apps.users.forms import BankDataRegistrationForm
from sejavoluntario.apps.users.forms import UserRegistrationForm

def userRegistration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
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

def addressRegistration(request):
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