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
from core.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-prof/', ProfileProfView.as_view(), name='profile-prof'),
    path('report-bug/', ReportBugView.as_view(), name='report-bug'),
    path('ask-team-change/', AskTeamChangeView.as_view(), name='ask-team-change'),
    path('matches/', MatchesView.as_view(), name='matches'),
    path('tournaments/', TorneiosView.as_view(), name='tournaments'),
    path('tournaments/<int:id>', TournamentView.as_view(), name='tournaments-id'),
    path('change-players/', ChangePlayersView.as_view(), name='change-players'),
    path('register-match/', RegisterMatchView.as_view(), name='register-match'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('list-team/', List_teamView.as_view(), name='list-team'),
    path("", include("social_django.urls"), name="social"),
    path('edit-team/<int:id>/', TeamEditar.as_view(), name='edit-team'),
    path('delete-team/<int:id>/', TeamRemover.as_view(), name='delete-team'),
    path('create-team/', TeamCriar.as_view(), name='create-team'),
    path('list_transfer/', listtransferView.as_view(), name='list_transfer'),
    
    path('chaveamento/<int:torneio_id>/', ChaveamentoView.as_view(), name='chaveamento'),
    path('register-tournament/', RegisterTournamentView.as_view(), name='register-tournament'),

]

