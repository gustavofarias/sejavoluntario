#!/usr/local/bin/python
# coding: utf-8

from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    passwd = forms.CharField(widget=forms.PasswordInput())
    repeat_passwd = forms.CharField(widget=forms.PasswordInput())
    
    def clean_email(self):
        try:
            User.objects.get(email=self.data.get('email'))
            raise forms.ValidationError(u"E-mail já cadastrado.")
        except User.DoesNotExist:
            pass

        return self.data.get('email')
    
    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        passwd = cleaned_data.get("passwd")
        repeat_passwd = cleaned_data.get("repeat_passwd")
        import ipdb;ipdb.set_trace()
        if passwd != repeat_passwd:
            raise forms.ValidationError("Passwd and Repeat passwd don't match.")

        return cleaned_data