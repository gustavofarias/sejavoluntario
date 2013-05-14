# coding: utf-8

from django.db import models


class Area (models.Model):
    type = models.FileField(upload_to='/image')
    document = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    celphone = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = "Areas"
        verbose_name = "Area"

    def __unicode__(self):
        return self.area.type
