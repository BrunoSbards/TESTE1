# Generated by Django 5.1.6 on 2025-02-14 02:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estado',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('sigla_estado', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='matricula',
            fields=[
                ('id_matricula', models.AutoField(primary_key=True, serialize=False)),
                ('numero_matricula', models.CharField(max_length=10)),
                ('sigla_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_leilao.estado')),
            ],
        ),
        migrations.CreateModel(
            name='leiloeiro',
            fields=[
                ('id_leiloeiro', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('telefone', models.CharField(max_length=15)),
                ('site', models.URLField(blank=True, null=True)),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_leilao.matricula')),
            ],
        ),
    ]
