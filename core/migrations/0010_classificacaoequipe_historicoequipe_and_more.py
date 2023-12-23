# Generated by Django 4.2.6 on 2023-12-22 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_usuario_url_foto_alter_usuario_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificacaoEquipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicao', models.IntegerField(default=0)),
                ('pontos_conquistados', models.IntegerField(default=0)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campeonato')),
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
        migrations.RemoveField(
            model_name='partida',
            name='nome_partida',
        ),
        migrations.RemoveField(
            model_name='equipe',
            name='tec_time',
        ),
        migrations.DeleteModel(
            name='Classificacao',
        ),
        migrations.AddField(
            model_name='historicoequipe',
            name='equipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.equipe'),
        ),
        migrations.AddField(
            model_name='classificacaoequipe',
            name='equipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.equipe'),
        ),
        migrations.AddField(
            model_name='equipe',
            name='tec_time',
            field=models.ForeignKey(default=1, limit_choices_to={'atuacao': 'T'}, on_delete=django.db.models.deletion.CASCADE, related_name='tecnico', to='core.jogador'),
            preserve_default=False,
        ),
    ]