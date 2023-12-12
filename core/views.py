from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, FormView
from django.views import View
from .forms import UsuarioForm

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

class RegisterTournamentView(TemplateView):
    template_name = 'register-tournament.html'

class ChangePlayersView(TemplateView):
    template_name = 'change-players.html'

class ChangeInformationsView(TemplateView):
    template_name = 'change-informations.html'

class RegisterMatchView(TemplateView):
    template_name = 'register-match.html'

class AdminBaseView(TemplateView):
    template_name = 'admin_base.html'
