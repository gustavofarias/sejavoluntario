from django.shortcuts import render
from sejavoluntario.apps.users.models import User
from sejavoluntario.apps.users.forms import UserRegistrationForm

def userRegistration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User()
            return HttpResponseRedirect('/thanks/')
    else:
        form = UserRegistrationForm()

    return render(request, 'userregistrationform.html', {
        'form': form,
    })
    
    
