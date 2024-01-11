# Generated by Django 4.2.6 on 2024-01-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_partida_torneio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='torneio',
        ),
        migrations.AddField(
            model_name='torneio',
            name='partidas',
            field=models.ManyToManyField(related_name='torneio_partidas', to='core.partida'),
        ),
    ]
