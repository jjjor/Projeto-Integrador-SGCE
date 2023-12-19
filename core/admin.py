from django.contrib import admin
from .forms import PartidaAdminForm
from .models import Campus, Jogador, Equipe, Classificacao, Modalidade, Partida, Resultado, Jogos, Campeonato, Usuario

# Register your models here.

admin.site.register(Usuario)
@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    list_filter = ('cidade',)
    search_fields = ('nome',)
    ordering = ('nome',)

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome_equipe', 'campus')
    list_filter = ('nome_equipe', 'campus', 'tec_time')
    search_fields = ('nome_equipe',)
    ordering = ('nome_equipe',)
    
@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'esporte', 'atuacao', 'sexo', 'campus')
    list_filter = ('campus', 'esporte', 'sexo', 'atuacao')
    search_fields = ('nome',)
    ordering = ('nome',)
    
@admin.register(Classificacao)
class ClassificacaoAdmin(admin.ModelAdmin):
    list_display = ('pontos_conquistados', 'posicao_Equipe', 'vitoria', 'empate', 'derrota')
    list_filter = ('posicao_Equipe',)
    search_fields = ('posicao_Equipe',)
    ordering = ('posicao_Equipe',)
    
@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo')
    list_filter = ('sexo',)
    search_fields = ('nome',)
    ordering = ('nome',)


class PartidaAdmin(admin.ModelAdmin):
    form = PartidaAdminForm
    list_display = ('nome_partida', 'campus_partida', 'display_times_partida')

    def display_times_partida(self, obj):
        return ', '.join([equipe.nome_equipe for equipe in obj.times_partida.all()])

    display_times_partida.short_description = 'Times da Partida'

admin.site.register(Partida, PartidaAdmin)
    
@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('data_inicio', 'data_final', 'campus_campeonato', 'modalidade_campeonato')
    list_filter = ('campus_campeonato', 'modalidade_campeonato')
    search_fields = ('campus_campeonato',)
    ordering = ('campus_campeonato',)

@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('jogo', 'pontos_equipe')
    list_filter = ('jogo',)
    search_fields = ('jogo',)
    ordering = ('jogo',)
    
@admin.register(Jogos)
class JogosAdmin(admin.ModelAdmin):
    list_display = ('campus', 'campeonato', 'data_jogo',)
    list_filter = ('campus','campeonato',)
    search_fields = ('campus',)
    ordering = ('campus',)
    
