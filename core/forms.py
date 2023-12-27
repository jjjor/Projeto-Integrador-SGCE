from django import forms
from .models import Usuario, Equipe, Partida, Torneio

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = '__all__'

class TorneioForm(forms.ModelForm):
    class Meta:
        model = Torneio
        fields = ['nome', 'data', 'equipes_torneio']
         
class PartidaAdminForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = ['esporte', 'time1', 'time2', 'data']


class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'
        
