# Generated by Django 4.2.6 on 2024-01-11 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_partida_torneio_torneio_partidas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='torneio',
            old_name='partidas',
            new_name='partida',
        ),
    ]
