from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Campus(models.Model):
    nome = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class Modalidade(models.Model):
    sexo_opcao = ('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')
    
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=sexo_opcao, default='M')
    
    def __str__(self):
        return self.nome
class Jogador(models.Model):
    
    sexo_opcao = ('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')
    atuacao_opcao = ('A', 'Atacante'), ('D', 'Defensor'), ('G', 'Goleiro'), ('T', 'Tecnico')
    
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    esporte = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    atuacao = models.CharField(max_length=1, choices=atuacao_opcao, default='A')
    sexo = models.CharField(max_length=1, choices=sexo_opcao, default='M')
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.nome
    
class Equipe(models.Model):
    nome_equipe = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    jogadores = models.ManyToManyField(Jogador)
    tec_time = models.ManyToManyField(Jogador, related_name='Tecnico', limit_choices_to={'atuacao': 'T'})
    
    def jogadores_do_campus(self): 
        return self.jogadores.filter(campus=self.campus)
    
    def __str__(self):
        return self.nome_equipe + " - " + self.campus.nome
    
class Partida(models.Model):
    nome_partida = models.CharField(max_length=100)
    campus_partida = models.ForeignKey(Campus, on_delete=models.CASCADE)
    times_partida = models.ManyToManyField(Equipe)
class Classificacao(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    vitoria = models.IntegerField(default=0)
    empate = models.IntegerField(default=0)
    derrota = models.IntegerField(default=0)
    posicao_Equipe = models.IntegerField(default=0)
    pontos_conquistados = models.IntegerField(default=0)

    def calcular_pontos(self):
        # Lógica para calcular os pontos
        self.pontos_conquistados = self.vitoria * 3 + self.empate
        self.save()

    def __str__(self):
        return f"{self.equipe} - Posição: {self.posicao_Equipe} - Pontos: {self.pontos_conquistados}"
class Resultado(models.Model):
    jogo = models.ForeignKey(Partida, on_delete=models.CASCADE)
    pontos_equipe = models.IntegerField()

@receiver(post_save, sender=Resultado)
def atualizar_classificacao(sender, instance, **kwargs):
    # Lógica para atualizar a classificação quando um resultado for salvo
    classificacoes = Classificacao.objects.all().order_by('-pontos_conquistados')
    posicao = 1
    for classificacao in classificacoes:
        classificacao.posicao_Equipe = posicao
        classificacao.save()
        posicao += 1
    
class Campeonato(models.Model):
    data_inicio = models.DateField()
    data_final = models.DateField()
    campus_campeonato = models.ForeignKey(Campus, on_delete=models.CASCADE)
    modalidade_campeonato = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    equipes_campeonato = models.ManyToManyField(Equipe)

    
class UserManager(BaseUserManager):

    def create_user(self, nome, email, password=None, campus=None, **extra_fields):
        if nome is None:
            raise TypeError('Usuário deve informar o nome')
        if email is None:
            raise TypeError('Usuário deve informar o email')

        user = self.model(nome=nome, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nome, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Certifique-se de que o campo campus está preenchido, mesmo que seja com uma instância fictícia de Campus
        return self.create_user(nome, email, password=password, **extra_fields)


class Jogos(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    equipe = models.ManyToManyField(Equipe)
    data_jogo = models.DateField()
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    resultado = models.OneToOneField(Resultado, on_delete=models.CASCADE, null=True, blank=True)
    
    def jogadores_do_campus(self):
        return self.equipe.filter(campus=self.campus)
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=42, unique=True)
    identificacao = models.CharField(max_length=64, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    senha = models.CharField(max_length=255)
    url_img = models.CharField(max_length=999, blank=True, null=True)
    # tipo_usuario = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    

    objects = UserManager()

    USERNAME_FIELD = "identificacao"
    REQUIRED_FIELDS = ['email']

    
