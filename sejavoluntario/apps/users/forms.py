#!/usr/local/bin/python
# coding: utf-8

from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.models import User
from django.db import transaction
from sejavoluntario.apps.users.models import Area
from sejavoluntario.apps.users.models import Banco
from sejavoluntario.apps.users.models import Beneficiario
from sejavoluntario.apps.users.models import Endereco
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
        
        return voluntario
    
class BeneficiarioRegistrationForm(forms.Form):
    
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())
    area = forms.MultipleChoiceField(choices=Area.objects.all(),
                                  widget=CheckboxSelectMultiple,
                                  label="Área de interesse",)
    site = forms.URLField()
    
    def __init__(self, *args, **kwargs):
        
        super(BeneficiarioRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['area'].choices = [(area.pk, area.name) for area in Area.objects.all()]
        
    
    def clean_email(self):
        try:
            User.objects.get(email=self.data.get('email'))
            raise forms.ValidationError(u"E-mail já cadastrado.")
        except User.DoesNotExist:
            logging.info("Email ainda não existe na base de dados")

        return self.data.get('email')
    
    def clean(self):
        cleaned_data = super(BeneficiarioRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")
        if password != repeat_password:
            raise forms.ValidationError("Passwd and Repeat passwd don't match.")

        return cleaned_data
    
    def save(self, *args, **kwargs):
        user = None

        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        area = self.cleaned_data.get('area')
        site = self.cleaned_data.get('site')
        username = email
        
        with transaction.commit_on_success():
            user = User.objects.create_user(username,email,password)
            user.first_name = name
            user.save()

            beneficiario = Beneficiario()
            beneficiario.user = user
            beneficiario.site = site
            beneficiario.save()

            beneficiario.areas = area
            beneficiario.save()
        
        return beneficiario

class BankDataRegistrationForm(forms.Form):
    banco = forms.ModelChoiceField(queryset=Banco.objects.all())
    agencia = forms.IntegerField()
    conta = forms.IntegerField()
    favorecido = forms.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        
        banco = self.cleaned_data.get('banco')
        agencia = self.cleaned_data.get('agencia')
        conta = self.cleaned_data.get('conta')
        favorecido = self.cleaned_data.get('favorecido')
        
        with transaction.commit_on_success():
            bank_data = DadosBancarios.objects.create_bank_data(banco=banco,
                                                                agencia=agencia,
                                                                conta=conta,
                                                                favorecido=favorecido)
        
        return bank_data
    
class AddressRegistrationForm(forms.Form):
    logradouro = forms.CharField(max_length=255)
    complemento = forms.CharField(max_length=255)
    cep = forms.IntegerField()
    numero = forms.IntegerField()

    def save(self, *args, **kwargs):
        
        logradouro = self.cleaned_data.get('logradouro')
        complemento = self.cleaned_data.get('complemento')
        cep = self.cleaned_data.get('cep')
        numero = self.cleaned_data.get('numero')
        
        with transaction.commit_on_success():
            address = Endereco.objects.create_address(logradouro=logradouro,
                                                      complemento=complemento,
                                                      cep=cep,
                                                      numero=numero)
        
        return address

class LoginForm(forms.Form):
    email = forms.CharField(max_length=50, label=u"Seu e-mail")
    password = forms.CharField(widget=forms.PasswordInput, max_length=100, label=u"Sua senha")

    def clean_email(self):
        try:
            User.objects.get( username = self.data.get('email') )
        except User.DoesNotExist:
            raise forms.ValidationError(u"Usuário inexistente.")
        
        return self.data.get('email')