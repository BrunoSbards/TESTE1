from django.db import models


class estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    sigla_estado = models.CharField(max_length=5)

class matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    numero_matricula = models.CharField(max_length=10)
    sigla_estado = models.ForeignKey(estado, on_delete=models.CASCADE)

class leiloeiro(models.Model):
    id_leiloeiro = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=15)
    site = models.URLField(blank=True, null=True)
    matricula = models.ForeignKey(matricula, on_delete=models.CASCADE)

