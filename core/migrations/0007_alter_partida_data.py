# Generated by Django 4.2.6 on 2023-12-25 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_partida_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='data',
            field=models.DateField(verbose_name='Data'),
        ),
    ]
