# Generated by Django 4.2.2 on 2023-06-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0006_experiencia_epoca_experiencia_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencia',
            name='descripcion',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='epoca',
            field=models.CharField(max_length=10),
        ),
    ]
