from django import forms
from .models import Usuario, Equipe, Partida, Torneio, Esporte, Campus

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = '__all__'
        widgets = {
            'nome_equipe': forms.TextInput(attrs={'id': 'nome_equipe'}),
            'campus': forms.Select(attrs={'id': 'campus'}),
            'jogadores': forms.SelectMultiple(attrs={'id': 'jogadores'}),
        }

class TorneioForm(forms.ModelForm):
    class Meta:
        model = Torneio
        fields = ['nome', 'data', 'equipes_torneio', 'esporte']
        widgets = {
            'nome': forms.TextInput(attrs={'id': 'nome'}),
            'esporte': forms.Select(attrs={'id': 'esporte'}),
            'data': forms.DateInput(attrs={'id': 'data', 'type': 'date'}),
            'equipes_torneio': forms.SelectMultiple(attrs={'id': 'equipes_torneio'}),
        }
         
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

class SportForm(forms.ModelForm):

    class Meta:
        model = Esporte
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'id': 'nome'}),
        }


class CampusForm(forms.ModelForm):

    class Meta:
        model = Campus
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'id': 'nome'}),
        }
