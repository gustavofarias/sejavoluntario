from django.shortcuts import render
from sejavoluntario.apps.users import models
from sejavoluntario.apps.users.forms import UserRegistrationForm

def userRegistration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            import ipdb;ipdb.set_trace()
            return HttpResponseRedirect('/thanks/')
    else:
        form = UserRegistrationForm()

    return render(request, 'userregistrationform.html', {
        'form': form,
    })
    
    
