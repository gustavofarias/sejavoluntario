# coding: utf-8
#!/usr/bin/env python

from django import forms
from django.contrib import admin

from sejavoluntario.apps.events import models

admin.site.register(models.Events)