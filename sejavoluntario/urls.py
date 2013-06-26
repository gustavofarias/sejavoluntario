# coding: utf-8
#!/usr/bin/env python

from django.contrib import admin
from django.conf.urls import patterns, include, url
from apps.core import views as coreViews
from apps.users import views as userViews

admin.autodiscover()

urlpatterns = patterns('',
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', coreViews.index),
    
    #ações logadas
    url(r'^me/?$', coreViews.logged_user, name="logged_user"),
    url(r'^me/profile/?$', userViews.user_profile, name="user_profile"),
    url(r'^user/change_password/?$', userViews.change_password, name="change_password"),
    
    #beneficiario
    url(r'^beneficiario/(?P<beneficiario_id>[0-9]+)/?$', userViews.show_beneficiario, name="show_beneficiario"),
    
    #json
    url(r'^beneficario/area-interesse/(?P<area>[0-9a-zA-Z]+)/bairro/(?P<bairro>[\w\+%_& ]+)?/qtd/(?P<qtd>[0-9]+)/?$', coreViews.lista_beneficiarios, name="lista_beneficiarios"),
    
    #login
    url(r'^user/login/?$', coreViews.user_login, name="user_login"),
    url(r'^user/logout/?$', coreViews.user_logout, name="user_logout"),
    
    #inserts
    url(r'^user/register/?$', userViews.userRegistration, name="user_registration"),
    url(r'^bank/register/?$', userViews.bankDataRegistration, name="bank_registration"),
    url(r'^address/register/?$', userViews.addressRegistration, name="address_registration"),
    url(r'^beneficiario/register/?$', userViews.beneficiarioRegistration, name="beneficiario_registration"),
    
)
