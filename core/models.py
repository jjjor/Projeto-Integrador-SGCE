from django.db import models
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
    tec_time = models.ManyToManyField(Jogador, related_name='tecnico', limit_choices_to={'atuacao': 'T'})
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    
    def jogadores_do_campus(self): 
        return self.jogadores.filter(campus=self.campus)
    
    def __str__(self):
        return self.nome_equipe + " - " + self.campus.nome
    
class Classificacao(models.Model):
    pontos_conquistados = models.IntegerField()
    posicao_Equipe = models.IntegerField()
    vitoria = models.IntegerField()
    empate = models.IntegerField()
    derrota = models.IntegerField()
    
    
class Partida(models.Model):
    nome_partida = models.CharField(max_length=100)
    campus_partida = models.ForeignKey(Campus, on_delete=models.CASCADE)
    times_partida = models.ManyToManyField(Equipe)
    
class Campeonato(models.Model):
    data_campeonato = models.DateField()
    campus_campeonato = models.ForeignKey(Campus, on_delete=models.CASCADE)
    modalidade_campeonato = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    equipes_campeonato = models.ManyToManyField(Equipe)

class Resultado(models.Model):
    jogo = models.ForeignKey(Partida, on_delete=models.CASCADE)
    pontos_equipe = models.IntegerField()
    
class UserManager(BaseUserManager):

    def create_user(self, nome_registro, email, password=None, campus='', tipo_usuario='', nome=''):
        if nome_registro is None:
            raise TypeError('Usuário deve informar o nome')
        else:
            nome_registro = nome_registro
        if email is None:
            raise TypeError('Users deve informar o Email')
        else:
            email = email
            
        if tipo_usuario == 'Aluno':
            aluno = tipo_usuario
    
    
        user = self.model(username=nome_registro, email=self.normalize_email(email), campus=campus, tipo_usuario=aluno, nome=nome)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, nome_registro, email, password=None, tipo_usuario=''):
        if password is None:
            raise TypeError('Password should not be none')
        if tipo_usuario == 'Professor':
            professor = tipo_usuario

        user = self.create_user(nome_registro, email, password, tipo_usuario=professor)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

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
    senha = models.CharField(max_length=255)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    tipo_usuario = models.CharField(max_length=40)
    

    objects = UserManager()

    USERNAME_FIELD = "nome"
    REQUIRED_FIELDS = ["email"]
    class Meta:
        verbose_name = "Usuário"

    def troca_de_time(self):
        
        return "Troca de time realizada com sucesso."

    def alterar_informacoes_pessoais(self):
        
        return "Informações pessoais alteradas com sucesso."

    def alterar_informacoes_seguranca(self):
        
        return "Informações de segurança alteradas com sucesso."
    
    
    
