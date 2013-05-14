#!/usr/local/bin/python
# coding: utf-8

from django import forms
from django.contrib.auth.models import User
from django.db import transaction
from sejavoluntario.apps.users.models import SejaVoluntarioUser


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())
    
    def clean_email(self):
        import ipdb;ipdb.set_trace()
        try:
            User.objects.get(email=self.data.get('email'))
            raise forms.ValidationError(u"E-mail já cadastrado.")
        except User.DoesNotExist:
            pass

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
        username = email
        
        with transaction.commit_on_success():
            user = User.objects.create_user(username,email,password)
            sejaVoluntarioUser = SejaVoluntarioUser()
            sejaVoluntarioUser.user = user
            sejaVoluntarioUser.save()
            user.save()
        
        return user