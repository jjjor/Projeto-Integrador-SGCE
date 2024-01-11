from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import EquipeForm, TorneioForm, ChangeTeamForm
from .forms import PartidaAdminForm
from django.urls import reverse_lazy
from .models import *

class IndexView(TemplateView):
    template_name = 'index.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'

class ProfileProfView(TemplateView):
    template_name = 'profile-prof.html'
    
class ReportBugView(TemplateView):
    template_name = 'report-bug.html'

class AskTeamChangeView(TemplateView):
    template_name = 'ask-team-change.html'
    form_class = ChangeTeamForm
    success_url = reverse_lazy('matches')
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ChangeTeamForm(request.POST)
        equipe_postada = request.POST.get('equipe')
        motivo = request.POST.get('motivo')
        equipe = Equipe.objects.get(id=equipe_postada)
        jogador = Usuario.objects.get(id=request.user.id)
        pedido = ChangeStudentTeam.objects.create(equipe=equipe, motivo=motivo, jogador=jogador)

        if form.is_valid():
            pedido.save()
            return redirect('ask-team-change')

        return redirect("matches")

class MatchesView(TemplateView):
    template_name = 'matches.html'

    def get(self, request, *args, **kwargs):
        partidas = Partida.objects.all()
        return render(request, self.template_name, {'partidas': partidas})

class RegisterTournamentView(CreateView):
    
    template_name = 'register-tournament.html'
    form_class = TorneioForm
    success_url = reverse_lazy('tournaments')
    
    def post(self, request, *args, **kwargs):
        form = TorneioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tournaments")
        else:
            HttpResponse("Formulário inválido")
        
        return redirect("tournaments", {'form': form})
    

def realizar_chaveamento(request, torneio_id):
    torneio = Torneio.objects.get(id=torneio_id)

    equipes = torneio.equipes_torneio.all()

    # Exemplo simples de chaveamento: dividir as equipes em pares
    jogos = []
    esporte_torneio = torneio.esporte  # Acesse a relação entre Torneio e Esporte

    for i in range(0, len(equipes), 2):
        jogo = Partida.objects.create(
            time1=equipes[i],
            time2=equipes[i + 1],
            esporte=esporte_torneio,  # Use o esporte do torneio
            data=torneio.data,
        )
        jogos.append(jogo)

    torneio.chaveamento_realizado = True
    torneio.save()

    return render(request, 'chave.html', {'jogos': jogos})
    

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


class EditTeam(UpdateView):
    template_name = 'edit-team.html'

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

class TeamCriar(CreateView):
    
    template_name = 'create-team.html'
    form_class = EquipeForm
    success_url = reverse_lazy('change-players')

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
    

class listtransferView(TemplateView):
    template_name = 'view-transfer.html'
    success_url = reverse_lazy('matches')

    def processar_transferencia(self, jogador, time_novo):
        print(f"Processando transferência de {jogador} para {time_novo}")

        # Obtenha todas as equipes antigas do jogador
        equipes_antigas = Equipe.objects.filter(jogadores=jogador)

        if equipes_antigas.exists():
            # Se houver equipes antigas, use a primeira encontrada
            equipe_antiga = equipes_antigas.first()
            print(f"Equipe antiga encontrada: {equipe_antiga}")
            
            # Remova o jogador da equipe antiga
            equipe_antiga.jogadores.remove(jogador)
        else:
            equipe_antiga = None
            print(f"O jogador {jogador} não está em nenhuma equipe antiga.")

        # Obtenha a equipe nova
        equipe_nova = get_object_or_404(Equipe, nome_equipe=time_novo)
        print(f"Equipe nova encontrada: {equipe_nova}")

        # Adicione o jogador à nova equipe
        equipe_nova.jogadores.add(jogador)

    def get(self, request, *args, **kwargs):
        pedidos = ChangeStudentTeam.objects.all()
        return render(request, self.template_name, {'pedidos': pedidos})

    def post(self, request, *args, **kwargs):
        print(request.POST)

        if request.POST.get('nome-jogador-reject'):
            nome_jogador = request.POST.get('nome-jogador-reject')
            jogador = Usuario.objects.get(full_name=nome_jogador)
            pedido = ChangeStudentTeam.objects.get(jogador=jogador)
            pedido.delete()
            return redirect('list_transfer')

        elif request.POST.get('nome-jogador'):
            nome_jogador = request.POST.get('nome-jogador')
            time_novo = request.POST.get('time-novo')

            if nome_jogador:  # Verifica se o nome do jogador não está vazio
                # Obtenha o jogador
                jogador = get_object_or_404(Usuario, full_name=nome_jogador)

                # Obtenha o pedido de transferência
                pedido = get_object_or_404(ChangeStudentTeam, jogador=jogador)
                
                # Processar transferência
                self.processar_transferencia(jogador, time_novo)

                # Excluir pedido após processamento
                pedido.delete()

        return redirect('list_transfer')
        

