import random
from faker import Faker
from django.core.management.base import BaseCommand
from core.models import *

fake = Faker()

class Command(BaseCommand):
    help = 'Populate data for your Django models using Faker'

    def handle(self, *args, **options):
        # Criação de Campi
        def create_campus():
            return Campus.objects.create(
                nome=fake.city(),
                cidade=fake.city()
            )

        # Criação de Modalidades
        def create_modalidade():
            return Modalidade.objects.create(
                nome=fake.word(),
                sexo=random.choice(['M', 'F', 'O'])
            )

        # Criação de Jogadores
        def create_jogador(campus, modalidade):
            return Jogador.objects.create(
                nome=fake.name(),
                idade=random.randint(18, 40),
                esporte=modalidade,
                atuacao=random.choice(['A', 'D', 'G', 'T']),
                sexo=random.choice(['M', 'F', 'O']),
                campus=campus
            )

        # Criação de Equipes
        def create_equipe(campus):
            return Equipe.objects.create(
                nome_equipe=fake.company(),
                campus=campus
            )

        # Adicionando Jogadores às Equipes
        def add_jogadores_to_equipe(equipe, jogadores):
            equipe.jogadores.set(jogadores)
            equipe.save()

        # Criação de Partidas
        def create_partida(campus):
            return Partida.objects.create(
                nome_partida=fake.word(),
                campus_partida=campus
            )

        # Criação de Resultados
        def create_resultado(partida):
            return Resultado.objects.create(
                jogo=partida,
                pontos_equipe=random.randint(0, 3)
            )

        # Criando os dados usando as funções definidas acima
        campus = create_campus()
        modalidade = create_modalidade()
        jogadores = [create_jogador(campus, modalidade) for _ in range(10)]
        equipe = create_equipe(campus)
        add_jogadores_to_equipe(equipe, jogadores)
        partida = create_partida(campus)
        resultado = create_resultado(partida)

        # Exemplo de uso para os demais modelos
        # ...

        # Salvando os dados criados no banco de dados
        campus.save()
        modalidade.save()
        for jogador in jogadores:
            jogador.save()
        equipe.save()
        partida.save()
        resultado.save()
        
        self.stdout.write(self.style.SUCCESS('Data populated successfully.'))