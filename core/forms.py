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
        widgets = { 
        }

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


class ChangeTeamForm(forms.Form):
    equipe = forms.ModelChoiceField(queryset=Equipe.objects.all(), empty_label=None)
    motivo = forms.CharField(max_length=200, widget=forms.Textarea)
