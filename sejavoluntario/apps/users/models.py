# coding: utf-8

from django.db import models
from django.contrib.auth.models import User


class SejaVoluntarioUser (models.Model):
    user = models.ForeignKey(User)
    photo = models.FileField(upload_to='/image')
    document = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    celphone = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = "Usuários"
        verbose_name = "Usuário"

    def __unicode__(self):
        return self.user.email
