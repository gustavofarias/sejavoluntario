# coding: utf-8
#!/usr/bin/env python

from django import forms
from django.contrib import admin

from sejavoluntario.apps.users import models

admin.site.register(models.UserProfile)
admin.site.register(models.Area)
admin.site.register(models.Endereco)
admin.site.register(models.Voluntario)
admin.site.register(models.Beneficiario)
admin.site.register(models.Banco)
admin.site.register(models.DadosBancarios)
