# Generated by Django 4.2.6 on 2024-01-11 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_torneio_chaveamento_realizado_torneio_esporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='campus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.campus'),
            preserve_default=False,
        ),
    ]
