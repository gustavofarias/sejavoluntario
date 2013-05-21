# coding: utf-8

from django.db import models
from django.contrib.auth.models import User


class Area (models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Áreas"
        verbose_name = "Área"

    def __unicode__(self):
        return self.name
    
class Pais(models.Model):
    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=2)
    pais = models.ForeignKey(Pais)

    def __unicode__(self):
        return u'{0} ({1})'.format(self.nome, self.pais.nome)


class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return u'{0} ({1})'.format(self.nome, self.estado.sigla)

class AddressManager(models.Manager):
    def create_address(self, logradouro, numero, complemento, cep):
        address = self.create(logradouro=logradouro,
                              numero=numero,
                              complemento=complemento,
                              cep=cep)
        return address

class Endereco(models.Model):
    logradouro = models.TextField(max_length=255,)
    numero = models.IntegerField(null=True, blank=True, default=None)
    complemento = models.CharField(max_length=255,null=True, blank=True, default=None)
    cep = models.IntegerField(max_length=6,)
    estado = models.ForeignKey(Estado, null=True, blank=True, default=None)
    cidade = models.ForeignKey(Cidade, null=True, blank=True, default=None)
    pais = models.ForeignKey(Pais, null=True, blank=True, default=None)
    
    objects = AddressManager()

    class Meta:
        verbose_name_plural = "Endereços"
        verbose_name = "Endereço"
        
    def __unicode__(self):
        return str(self.cep)
        

class UserProfile (models.Model):
    user = models.ForeignKey(User)
    photo = models.FileField(upload_to='/image')
    document = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    celphone = models.CharField(max_length=20)
    
    areas = models.ManyToManyField(Area)
    endereco = models.ForeignKey(Endereco, default=None, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Usuários"
        verbose_name = "Usuário"

    def __unicode__(self):
        return self.user.email

class Voluntario(UserProfile):
    #participacoes = models.ManyToManyField(Campanha,
        #help_text = "Campanhas que o usuario participou", null=True, blank=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    nascimento = models.DateTimeField(blank=True, null=True)
    
class Banco(models.Model):
    nome = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.nome

class BankDataManager(models.Manager):
    def create_bank_data(self, banco, agencia, conta, favorecido):
        bank_data = self.create(banco=banco, agencia=agencia, conta=conta, favorecido=favorecido)
        return bank_data
    
class DadosBancarios(models.Model):
    agencia = models.IntegerField()
    conta = models.IntegerField()
    favorecido = models.CharField(max_length=40)
    
    banco = models.ForeignKey(Banco)
    
    objects = BankDataManager()
    
    class Meta:
        verbose_name_plural = "Dados Bancários"
        verbose_name = "Dados Bancários"
        
    def __unicode__(self):
        return self.favorevido

class Beneficiario(UserProfile):
    banco = models.ForeignKey(DadosBancarios, null=True, blank=True, default=None)
    site = models.URLField(null=True, blank=True, default=None)