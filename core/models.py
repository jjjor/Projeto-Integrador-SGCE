from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Campus(models.Model):

    nome = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Jogador(models.Model):

    sexo_opcao = ('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    esporte = models.ForeignKey('Esporte', on_delete=models.CASCADE, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=sexo_opcao, default='M')
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Equipe(models.Model):
    
    nome_equipe = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True, blank=True)
    jogadores = models.ManyToManyField('Jogador')

    def jogadores_do_campus(self):
        return self.jogadores.filter(campus=self.campus)

    def __str__(self):
        return self.nome_equipe
    
class HistoricoEquipe(models.Model):

    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    vitoria = models.IntegerField(default=0)
    derrota = models.IntegerField(default=0)
    empate = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Histórico de {self.equipe} - Vitórias: {self.vitorias} / Derrotas: {self.derrotas}"

    def registrar_vitoria(self):
        self.vitoria += 1
        self.save()

    def registrar_derrota(self):
        self.derrota += 1
        self.save()

class Torneio(models.Model):

    nome = models.CharField(max_length=100)
    data = models.DateField()
    equipes_torneio = models.ManyToManyField(Equipe)
    
    
class ClassificacaoEquipe(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE,null=True, blank=True)
    torneio = models.ForeignKey(Torneio, on_delete=models.CASCADE, null=True, blank=True)
    posicao = models.IntegerField(default=0)
    pontos_conquistados = models.IntegerField(default=0)

    def calcular_pontos(self):
        # Lógica para calcular os pontos
        vitorias_equipe = Resultado.objects.filter(jogo__torneio=self.torneio, jogo__equipe=self.equipe, pontos_equipe__gt=0).count()
        self.pontos_conquistados = vitorias_equipe * 3
        self.save()

    def atualizar_posicao(self):
        # Atualiza a posição da equipe com base nos pontos conquistados
        classificacoes = ClassificacaoEquipe.objects.filter(torneio=self.torneio).order_by('-pontos_conquistados')
        posicao = 1
        for classificacao in classificacoes:
            classificacao.posicao = posicao
            classificacao.save()
            posicao += 1

        # Atualiza a posição da equipe atual
        self.posicao = posicao
        self.save()
        
    def __str__(self):
        return f"Classificação de {self.equipe} no {self.torneio} - Posição: {self.posicao} - Pontos: {self.pontos_conquistados}"
    
    
# class Partida(models.Model):

#     data =  models.DateField(default='2023-01-01')
#     campus_partida = models.ForeignKey(Campus, on_delete=models.CASCADE)
#     times_partida = models.ManyToManyField(Equipe)
    
#     def __str__(self):
#         return f"Partida entre {self.times_partida.all()[0]} e {self.times_partida.all()[1]}"
    
class Esporte(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Partida(models.Model):

    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField("Data")
    time1 = models.ForeignKey(Equipe, on_delete=models.CASCADE, null=True, blank=True, related_name='partidas_time1')
    time2 = models.ForeignKey(Equipe, on_delete=models.CASCADE, null=True, blank=True, related_name='partidas_time2')
    placar = models.CharField("Placar", default="0x0", max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.time1} {self.placar} {self.time2} - ({self.esporte})"
    
class Resultado(models.Model):
    jogo = models.ForeignKey(Partida, on_delete=models.CASCADE, null=True, blank=True)
    pontos_equipe = models.IntegerField()

@receiver(post_save, sender=Resultado)
def atualizar_classificacao(sender, instance, **kwargs):
    # Lógica para atualizar a classificação quando um resultado for salvo
    classificacoes = Equipe.objects.all().order_by('- pontos_conquistados')
    posicao = 1
    for classificacao in classificacoes:
        classificacao.posicao_Equipe = posicao
        classificacao.save()
        posicao += 1

class UserManager(BaseUserManager):

    def create_user(self, identification,email, full_name="", role="", url_foto="", password=None, **extra_fields):

        if identification is None:
            raise TypeError('Usuário deve informar o identification')

        if role == "Professor":
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
        elif role == "Aluno":
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)
        
        user = self.model(
            identification=identification,
            email=self.normalize_email(email),
            usual_name=full_name,
            role=role,
            url_foto=url_foto,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
    
        return user

    def create_superuser(self, identification, email, password=None,**extra_fields):
        print("Extra Fields:")
        for key, value in extra_fields.items():
            print(f"{key}: {value}")
            
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(identification, email, password=password, **extra_fields)
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    identification = models.CharField(max_length=255, unique=True, default="20222094040001")
    usual_name = models.CharField(max_length=255, default="Usuário")
    role = models.CharField(max_length=255, default='Professor')
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=False, null=True)
    url_foto = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "identification"
    REQUIRED_FIELDS = ['email', 'full_name', 'role', 'url_foto']
    
class Jogos(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True, blank=True)
    equipe = models.ManyToManyField(Equipe)
    data_jogo = models.DateField()
    torneio = models.ForeignKey(Torneio, on_delete=models.CASCADE, null=True, blank=True)
    resultado = models.OneToOneField(
        Resultado, on_delete=models.CASCADE, null=True, blank=True)

    def jogadores_do_campus(self):
        return self.equipe.filter(campus=self.campus)

