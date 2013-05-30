from django.db import models

from sejavoluntario.apps.users.models import Endereco
from sejavoluntario.apps.users.models import UserProfile

class Events(models.Model):
    name = models.CharField(max_length = 30, default = "Evento")
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='campanha/', blank=True, null=True)
    
    address = models.ForeignKey(Endereco, default=None, null=True, blank=True)
    creator = models.ForeignKey(UserProfile, related_name='creator')
    
    members = models.ManyToManyField(UserProfile,
        null=True, blank=True, related_name='members',
        help_text = "Usuario que participaram dessa campanha")
    
    class Meta:
        verbose_name_plural = "Eventos"
        verbose_name = "Evento"