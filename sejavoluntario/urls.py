from django.contrib import admin
from django.conf.urls import patterns, include, url
from apps.core import views as coreViews
from apps.users import views as userViews

admin.autodiscover()

urlpatterns = patterns('',
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', coreViews.index),
    url(r'^user/register/?$', userViews.userRegistration, name="user_registration"),
    url(r'^bank/register/?$', userViews.bankRegistration, name="bank_registration"),
    
)
