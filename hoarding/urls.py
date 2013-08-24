from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hoarding.views.home', name='home'),
    # url(r'^hoarding/', include('hoarding.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'hoardingusers.views.HoardingUserRegistration'),
    
    url(r'^login/$', 'hoardingusers.views.LoginRequest'),    
    url(r'^logout/$', 'hoardingusers.views.LogoutRequest'),
    
    url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset'),
    url(r'^reset/done$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^profile/$', 'hoardingusers.views.Profile'),
    
    url(r'^hoarding/$', 'hoarding.views.AddHoarding'),
)
