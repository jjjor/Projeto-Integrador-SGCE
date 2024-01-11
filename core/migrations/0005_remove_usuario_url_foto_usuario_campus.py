# Generated by Django 4.2.6 on 2024-01-11 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_usuario_campus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='url_foto',
        ),
        migrations.AddField(
            model_name='usuario',
            name='campus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.campus'),
        ),
    ]