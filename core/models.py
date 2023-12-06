from django.db import models

class Campus(models.Model):
    name = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Jogador(models.Model):
    
    sexo_opcao = ('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')
    
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    esporte = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=sexo_opcao, default='M')
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    
class Equipe(models.Model):
    nome_equipe = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    jogadores = models.ManyToManyField(Jogador)
    tec_time = models.ManyToManyField(Jogador, related_name='tecnico')
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    
    def jogadores_do_campus(self):
        return self.jogadores.filter(campus=self.campus)
    
class Classificacao(models.Model):
    pontos_conquistados = models.IntegerField()
    posicao_Equipe = models.IntegerField()
    vitoria = models.IntegerField()
    empate = models.IntegerField()
    derrota = models.IntegerField()
    
class Modalidade(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=Jogador.sexo_opcao, default='M')
    
class Partida(models.Model):
    nome_partida = models.CharField(max_length=100)
    times_partida = models.ManyToManyField(Equipe)
    
class Campeonato(models.Model):
    data_campeonato = models.DateField()
    campus_campeonato = models.ForeignKey(Campus, on_delete=models.CASCADE)
    modalidade_campeonato = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    equipes_campeonato = models.ManyToManyField(Equipe)

class Resultado(models.Model):
    jogo = models.ForeignKey(Partida, on_delete=models.CASCADE)
    pontos_equipe = models.IntegerField()

class Jogos(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    equipe = models.ManyToManyField(Equipe)
    data_jogo = models.DateField()
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    resultado = models.OneToOneField(Resultado, on_delete=models.CASCADE, null=True, blank=True)
    
    def jogadores_do_campus(self):
        return self.equipe.filter(campus=self.campus)
    
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def troca_de_time(self):
        
        return "Troca de time realizada com sucesso."

    def alterar_informacoes_pessoais(self):
        
        return "Informações pessoais alteradas com sucesso."

    def alterar_informacoes_seguranca(self):
        
        return "Informações de segurança alteradas com sucesso."
    
    
    
