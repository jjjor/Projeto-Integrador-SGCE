from django.contrib import admin
from .forms import PartidaAdminForm
from .models import Campus, Jogador, Equipe, ClassificacaoEquipe, Partida, Resultado, Jogos, Torneio, Usuario, Esporte

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
    list_filter = ('nome_equipe', 'campus')
    search_fields = ('nome_equipe',)
    ordering = ('nome_equipe',)

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'esporte', 'sexo', 'campus')
    list_filter = ('campus', 'esporte', 'sexo')
    search_fields = ('nome',)
    ordering = ('nome',)
    
@admin.register(ClassificacaoEquipe)
class ClassificacaoAdmin(admin.ModelAdmin):
    list_display = ('posicao', 'equipe', 'pontos_conquistados')
    list_filter = ('posicao',)
    search_fields = ('posicao',)
    ordering = ('posicao',)

class PartidaAdmin(admin.ModelAdmin):
    form = PartidaAdminForm
    display = ('display_times_partida')

    def display_times_partida(self, obj):
        return ', '.join([equipe.nome_equipe for equipe in obj.times_partida.all()])

    display_times_partida.short_description = 'Times da Partida'

admin.site.register(Partida, PartidaAdmin)
    

@admin.register(Torneio)
class TorneioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data')
    list_filter = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)

@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('jogo', 'pontos_equipe')
    list_filter = ('jogo',)
    search_fields = ('jogo',)
    ordering = ('jogo',)
    
@admin.register(Jogos)
class JogosAdmin(admin.ModelAdmin):
    list_display = ('campus', 'torneio', 'data_jogo',)
    list_filter = ('campus','torneio',)
    search_fields = ('campus',)
    ordering = ('campus',)
    
@admin.register(Esporte)
class EsporteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome', )
