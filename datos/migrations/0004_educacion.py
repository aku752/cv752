# Generated by Django 4.2.2 on 2023-06-21 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0003_delete_educasion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educasion', models.CharField(max_length=100)),
                ('epoca', models.IntegerField()),
                ('colegio', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
