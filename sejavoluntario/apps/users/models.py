from django.db import models
from django.contrib.auth.models import User


class User (models.Model):
    user = models.ForeignKey(User)
    photo = models.FileField(upload_to='/image')
    document = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    celphone = models.CharField(max_length=20)

    def __unicode__(self):
            return u"%s" % self.id
        
    def register(self):
        pass