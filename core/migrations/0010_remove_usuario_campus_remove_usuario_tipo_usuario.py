# Generated by Django 4.2.6 on 2023-12-13 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_usuario_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='campus',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipo_usuario',
        ),
    ]