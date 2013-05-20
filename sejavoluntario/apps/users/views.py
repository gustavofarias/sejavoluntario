from django.shortcuts import render
from sejavoluntario.apps.users.forms import UserRegistrationForm
from sejavoluntario.apps.users.forms import BankRegistrationForm

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
    
def bankRegistration(request):
    if request.method == 'POST':
        form = BankRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
    else:
        form = BankRegistrationForm()

    return render(request, 'bankregistrationform.html', {
        'form': form,
    })