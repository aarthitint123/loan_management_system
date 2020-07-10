"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import login_view, register_view, logout_view, app_view
from django.urls import path, include   # new
from django.views.generic import TemplateView



from django.conf.urls import url, include
from django.contrib import admin
from accounts import views
from.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('accounts/login/',login_view),
    path('accounts/login/accounts/signup/', register_view),
    path('accounts/signup/accounts/login/', login_view),

    path('accounts/signup/', register_view),
    path('accounts/logout/', logout_view),
    path('accounts/create/', app_view),
    #path('accounts/update/', views.Application_Update.as_view()),
    #path('accounts/<int:pk>/delete/', views.Application_Delete.as_view()),

    url(r'^oauth/', include('social_django.urls', namespace='social')),







    #path('dtcc_prac/', include('django.contrib.auth.urls')),       # new
    #path('', TemplateView.as_view(template_name='home.html'), name='home'), # new

    #path('signup/',TemplateView.as_view(template_name='signup.html'), name='registration_page'),
    #url for app
    #path('accounts/', include('accounts.urls')),    # new


]
