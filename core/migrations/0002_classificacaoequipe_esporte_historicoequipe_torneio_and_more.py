# Generated by Django 4.2.6 on 2023-12-25 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificacaoEquipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicao', models.IntegerField(default=0)),
                ('pontos_conquistados', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Esporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoEquipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vitoria', models.IntegerField(default=0)),
                ('derrota', models.IntegerField(default=0)),
                ('empate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Torneio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='classificacao',
            name='equipe',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='senha',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='equipe',
            name='tec_time',
        ),
        migrations.RemoveField(
            model_name='jogador',
            name='atuacao',
        ),
        migrations.RemoveField(
            model_name='jogos',
            name='campeonato',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='campus_partida',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='nome_partida',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='times_partida',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='identificacao',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='url_img',
        ),
        migrations.AddField(
            model_name='partida',
            name='data',
            field=models.DateField(default='2023-01-01'),
        ),
        migrations.AddField(
            model_name='partida',
            name='placar_casa',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='partida',
            name='placar_visitante',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='partida',
            name='time1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='time2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='identification',
            field=models.CharField(default='20222094040001', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='role',
            field=models.CharField(default='Professor', max_length=255),
        ),
        migrations.AddField(
            model_name='usuario',
            name='url_foto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usual_name',
            field=models.CharField(default='Usuário', max_length=255),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='campus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.campus'),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='campus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.campus'),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='esporte',
            field=models.CharField(max_length=50, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='jogos',
            name='campus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.campus'),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='jogo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.partida'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Campeonato',
        ),
        migrations.DeleteModel(
            name='Classificacao',
        ),
        migrations.DeleteModel(
            name='Modalidade',
        ),
        migrations.AddField(
            model_name='torneio',
            name='equipes_torneio',
            field=models.ManyToManyField(to='core.equipe'),
        ),
        migrations.AddField(
            model_name='historicoequipe',
            name='equipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.equipe'),
        ),
        migrations.AddField(
            model_name='classificacaoequipe',
            name='equipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.equipe'),
        ),
        migrations.AddField(
            model_name='classificacaoequipe',
            name='torneio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.torneio'),
        ),
        migrations.AddField(
            model_name='jogos',
            name='torneio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.torneio'),
        ),
        migrations.AddField(
            model_name='partida',
            name='esporte',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.esporte'),
        ),
    ]
