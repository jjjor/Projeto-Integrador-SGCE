from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Campus(models.Model):

    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.nome}"
    

class Equipe(models.Model):
    
    nome_equipe = models.CharField(max_length=100)
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE, null=True, blank=True)
    jogadores = models.ManyToManyField('Usuario')

    def __str__(self):
        return self.nome_equipe
    
class HistoricoEquipe(models.Model):

    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    vitoria = models.IntegerField(default=0)
    derrota = models.IntegerField(default=0)
    empate = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Histórico de {self.equipe} - Vitórias: {self.vitorias} / Derrotas: {self.derrotas}"

class Partida(models.Model):

    esporte = models.ForeignKey('Esporte', on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField("Data")
    time1 = models.ForeignKey(Equipe, on_delete=models.CASCADE, null=True, blank=True, related_name='partidas_time1')
    time2 = models.ForeignKey(Equipe, on_delete=models.CASCADE, null=True, blank=True, related_name='partidas_time2')
    placar = models.CharField("Placar", default="0x0", max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.time1} {self.placar} {self.time2} - ({self.esporte})"
    
class Torneio(models.Model):
    
    partida = models.ManyToManyField('Partida', related_name='torneio_partidas')
    nome = models.CharField(max_length=100)
    data = models.DateField()
    esporte = models.ForeignKey('Esporte', on_delete=models.CASCADE, null=True, blank=True)
    equipes_torneio = models.ManyToManyField(Equipe)
    chaveamento_realizado = models.BooleanField(default=False)
    
    
class ClassificacaoEquipe(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE,null=True, blank=True)
    torneio = models.ForeignKey(Torneio, on_delete=models.CASCADE, null=True, blank=True)
    posicao = models.IntegerField(default=0)
    pontos_conquistados = models.IntegerField(default=0)
    
    
class Esporte(models.Model):

    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
    
class Resultado(models.Model):
    jogo = models.ForeignKey(Partida, on_delete=models.CASCADE, null=True, blank=True)
    pontos_equipe = models.IntegerField()


class UserManager(BaseUserManager):

    def create_user(self, identification, email, full_name="", role="", password=None, **extra_fields):

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
            full_name=full_name,
            role=role,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
    
        return user

    def create_superuser(self, identification, email, password=None,**extra_fields):
        # print("Extra Fields:")
        # for key, value in extra_fields.items():
        #     print(f"{key}: {value}")
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(identification, email, password=password, **extra_fields)
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    identification = models.CharField(max_length=255, unique=True, default="20222094040001")
    role = models.CharField(max_length=255, default='Professor')
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE, null=True, blank=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "identification"
    REQUIRED_FIELDS = ['email', 'full_name', 'role']
    
    def __str__(self):
        return f"{self.full_name}"
    
    
class Jogos(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True, blank=True)
    equipe = models.ManyToManyField(Equipe)
    data_jogo = models.DateField()
    torneio = models.ForeignKey(Torneio, on_delete=models.CASCADE, null=True, blank=True)
    resultado = models.OneToOneField(
        Resultado, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.campus} - {self.data_jogo} - {self.torneio}"

class ChangeStudentTeam(models.Model):
    motivo = models.CharField(max_length=100)
    jogador = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.jogador} - {self.equipe} - {self.motivo}"
    
    class Meta:
        verbose_name = "Pedido de Transferência"
        verbose_name_plural = "Pedidos de Transferência"