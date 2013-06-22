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
    
    #login
    url(r'^user/login/?$', coreViews.user_login, name="user_login"),
    url(r'^user/logout/?$', coreViews.user_logout, name="user_logout"),
    
    #registros
    url(r'^user/register/?$', userViews.userRegistration, name="user_registration"),
    url(r'^bank/register/?$', userViews.bankDataRegistration, name="bank_registration"),
    url(r'^address/register/?$', userViews.addressRegistration, name="address_registration"),
    url(r'^beneficiario/register/?$', userViews.beneficiarioRegistration, name="beneficiario_registration"),
    
)
