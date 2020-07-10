from django.conf.urls import url
from django.contrib.auth import login,logout

from . import views

urlpatterns = [


    url(r'^$',login,{'template_name': 'registration/login.html'}),
    url(r'^$',logout,{'template_name': 'registration/logout.html'})

    ]