# Generated by Django 2.2.3 on 2019-07-30 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_ideia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideia',
            name='categorias',
            field=models.CharField(choices=[('TERRA_PLANA', 'Terra Plana'), ('CONTRA_GROGER', 'Ideias para Coach Groger'), ('CONTRA_JOAO', 'Ideias contra João'), ('PUBLICAS', 'Públicas'), ('OUTROS', 'Outros')], max_length=255, verbose_name='Categoria'),
        ),
    ]
