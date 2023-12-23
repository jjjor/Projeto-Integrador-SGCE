from django import forms
from .models import Usuario, Equipe, Partida

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
         
class PartidaAdminForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Se já existirem 2 equipes associadas à partida, desabilita as outras opções
        if 'times_partida' in self.fields and self.fields['times_partida'].queryset.count() >= 2:
            self.fields['times_partida'].widget.attrs['disabled'] = True

class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'
        
