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
from django.urls import path, include
from core import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    # path('login/', include('django.contrib.auth.urls')),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('profile-prof', views.profile_prof, name='profile-prof'),
    path('info-security', views.info_security, name='info_security'),
    path('info-pessoal', views.info_pessoal, name='info_pessoal'),
    path('report-bug', views.report_bug, name='report-bug'),
    path('report-bug', views.report_bug, name='report_bug'),
    path('rating', views.rating, name='rating'),
    path('ask-team-change', views.ask_team_change, name='ask-team-change'),
    path('matches', views.matches, name='matches'),
    path('register-tournament', views.register_tournament, name='register-tournament'),
    path('change-players', views.change_players, name='change-players'),
    path('change-informations', views.change_informations, name='change-informations'),
    path('register-match', views.register_match, name='register-match'),
    path('admin_base', views.admin_base, name='admin_base')
]

