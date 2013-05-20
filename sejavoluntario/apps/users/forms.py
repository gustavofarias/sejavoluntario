#!/usr/local/bin/python
# coding: utf-8

from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.models import User
from django.db import transaction
from sejavoluntario.apps.users.models import Area
from sejavoluntario.apps.users.models import Banco
from sejavoluntario.apps.users.models import UserProfile
from sejavoluntario.apps.users.models import Voluntario

import logging

class UserRegistrationForm(forms.Form):
    
    SEX_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())
    data_nascimento = forms.DateField()
    sexo = forms.ChoiceField(choices=SEX_CHOICES)
    area = forms.MultipleChoiceField(choices=Area.objects.all(),
                                  widget=CheckboxSelectMultiple,
                                  label="Área de interesse",)
    
    def __init__(self, *args, **kwargs):
        
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['area'].choices = [(area.pk, area.name) for area in Area.objects.all()]
        
    
    def clean_email(self):
        try:
            User.objects.get(email=self.data.get('email'))
            raise forms.ValidationError(u"E-mail já cadastrado.")
        except User.DoesNotExist:
            logging.info("Email ainda não existe na base de dados")

        return self.data.get('email')
    
    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")
        if password != repeat_password:
            raise forms.ValidationError("Passwd and Repeat passwd don't match.")

        return cleaned_data
    
    def save(self, *args, **kwargs):
        user = None

        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        sexo = self.cleaned_data.get('sexo')
        data_nascimento = self.cleaned_data.get('data_nascimento')
        area = self.cleaned_data.get('area')
        username = email
        
        with transaction.commit_on_success():
            user = User.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            
            voluntario = Voluntario()
            voluntario.user = user
            voluntario.sexo = sexo
            voluntario.nascimento = data_nascimento
            voluntario.save()

            voluntario.areas = area
            voluntario.save()
        
        return user
    
class BankRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        
        name = self.cleaned_data.get('name')
        
        with transaction.commit_on_success():
            bank = Banco.objects.create_bank(name)
        
        return bank