from django.contrib import admin
from django.conf.urls import patterns, include, url
from apps.core import views as coreViews
from apps.users import views as userViews

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', coreViews.index),
    url(r'^user/register/?$', userViews.userRegistration, name="user_registration"),
    
)
