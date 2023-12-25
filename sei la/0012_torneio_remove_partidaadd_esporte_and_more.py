# Generated by Django 4.2.6 on 2023-12-25 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_esporte_partida_data_partidaadd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Torneio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='partidaadd',
            name='esporte',
        ),
        migrations.RemoveField(
            model_name='classificacaoequipe',
            name='campeonato',
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
            name='times_partida',
        ),
        migrations.AddField(
            model_name='partida',
            name='esporte',
            field=models.ForeignKey(default='Futebol', on_delete=django.db.models.deletion.CASCADE, to='core.esporte'),
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
            field=models.CharField(default='Time 1', max_length=50),
        ),
        migrations.AddField(
            model_name='partida',
            name='time2',
            field=models.CharField(default='Time 2', max_length=50),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='esporte',
            field=models.CharField(max_length=50, verbose_name=''),
        ),
        migrations.DeleteModel(
            name='Campeonato',
        ),
        migrations.DeleteModel(
            name='Modalidade',
        ),
        migrations.DeleteModel(
            name='PartidaAdd',
        ),
        migrations.AddField(
            model_name='torneio',
            name='equipes_torneio',
            field=models.ManyToManyField(to='core.equipe'),
        ),
        migrations.AddField(
            model_name='classificacaoequipe',
            name='torneio',
            field=models.ForeignKey(default='Intercurso', on_delete=django.db.models.deletion.CASCADE, to='core.torneio'),
        ),
        migrations.AddField(
            model_name='jogos',
            name='torneio',
            field=models.ForeignKey(default='Intercurso', on_delete=django.db.models.deletion.CASCADE, to='core.torneio'),
        ),
    ]
