from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import EquipeForm, TorneioForm
from .forms import UsuarioForm
from .forms import PartidaAdminForm
from django.urls import reverse_lazy
from .models import *

class IndexView(TemplateView):
    template_name = 'index.html'

class CadastrarUsuarioView(FormView):
    template_name = 'register.html'
    form_class = UsuarioForm
    success_url = 'pagina_sucesso'  # Redireciona para uma página de sucesso

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # Redirecione para a página desejada após o login
            return redirect('página_de_sucesso')
        else:
            # Lógica para lidar com credenciais inválidas
            # Pode adicionar uma mensagem de erro, etc.
            return render(request, self.template_name, {'erro': 'Credenciais inválidas'})

class ProfileView(TemplateView):
    template_name = 'profile.html'

class ProfileProfView(TemplateView):
    template_name = 'profile-prof.html'

class InfoSecurityView(TemplateView):
    template_name = 'info-security.html'

class InfoPessoalView(TemplateView):
    template_name = 'info-pessoal.html'

class ReportBugView(TemplateView):
    template_name = 'report-bug.html'

class RatingView(TemplateView):
    template_name = 'rating.html'

class AskTeamChangeView(TemplateView):
    template_name = 'ask-team-change.html'

class MatchesView(TemplateView):
    template_name = 'matches.html'

    def get(self, request, *args, **kwargs):
        partidas = Partida.objects.all()
        return render(request, self.template_name, {'partidas': partidas})

class RegisterTournamentView(CreateView):
    
    template_name = 'register-tournament.html'
    form_class = TorneioForm
    success_url = reverse_lazy('matches')

class TorneiosView(TemplateView):
    template_name = 'tournaments.html'

    def get(self, request, *args, **kwargs):
        torneios = Torneio.objects.all()
        return render(request, self.template_name, {'torneios': torneios})
    
class TournamentView(TemplateView):
    template_name = 'tournament.html'

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id is None:
            return redirect('tournaments')
        torneio = Torneio.objects.get(id=id)
        return render(request, self.template_name, {'torneio': torneio})

class ChangePlayersView(TemplateView):
    template_name = 'change-players.html'

    def get(self, request, *args, **kwargs):

        times = Equipe.objects.all()

        return render(request, self.template_name, {'times': times})

    def post(self, request, *args, **kwargs):
       
        if form.is_valid():

            return redirect("matches")
        return redirect("matches")

class EditTeam(UpdateView):
    template_name = 'edit-team.html'


class ChangeInformationsView(TemplateView):
    template_name = 'change-informations.html'

class RegisterMatchView(TemplateView):

    template_name = 'register-match.html'

    def get(self, request, *args, **kwargs):
        form = PartidaAdminForm()
        equipes = Equipe.objects.all()
        esportes = Esporte.objects.all()
        return render(request, self.template_name, {'form': form, 'equipes': equipes, 'esportes': esportes})

    def post(self, request, *args, **kwargs):
        form = PartidaAdminForm(request.POST)
        change_sport = request.POST.get('change-sport')
        time1 = request.POST.get('time1')
        time2 = request.POST.get('time2')
        date = request.POST.get('date')

        esporte = Esporte.objects.get(nome=change_sport)

        equipe1 = Equipe.objects.get(nome_equipe=time1)
        equipe2 = Equipe.objects.get(nome_equipe=time2)

        partida = Partida.objects.create(esporte=esporte, time1=equipe1, time2=equipe2, data=date)

        if form.is_valid():
            partida.save()
            return redirect("matches")
        return redirect("matches")

class AdminBaseView(TemplateView):
    template_name = 'admin_base.html'

class TeamCriar(CreateView):
    
    template_name = 'create-team.html'
    form_class = EquipeForm
    success_url = reverse_lazy('create-team')

class TeamEditar(UpdateView):
    model = Equipe
    form_class = EquipeForm
    template_name = 'edit-team.html'
    pk_url_kwarg = 'id' # Nome da variável na URL
    
    def get_success_url(self):
        return reverse_lazy('change-players')

class TeamRemover(DeleteView):
    model = Equipe
    success_url = reverse_lazy('change-players')  
    pk_url_kwarg = 'id'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class TeamCreateView(CreateView):
    template_name = 'create-team.html'
    form_class = EquipeForm
    success_url = reverse_lazy('change-players')


class List_teamView(TemplateView):
    template_name = 'list-teams.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['teams'] = Equipe.objects.all()
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)

