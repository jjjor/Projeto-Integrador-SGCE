# Generated by Django 4.2.6 on 2023-12-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_usuario_email_remove_usuario_identificacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='identification',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
