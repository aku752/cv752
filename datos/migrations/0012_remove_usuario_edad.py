# Generated by Django 4.2.2 on 2023-06-24 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0011_usuario_ciudad_usuario_pais'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='edad',
        ),
    ]
