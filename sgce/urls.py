"""
URL configuration for sgce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('profile-prof', views.profile_prof, name='profile-prof'),
    path('info-security', views.info_security, name='info_security'),
    path('info-pessoal', views.info_pessoal, name='info_pessoal'),
    path('report-bug', views.report_bug, name='report-bug'),
    path('report-bug', views.report_bug, name='report_bug'),
    path('matches', views.matches, name='matches'),
]

