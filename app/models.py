from django.db import models

class Empresas(models.Model):
    cnpj = models.CharField(max_length=14)
    nome = models.CharField(max_length=500)
    descricao = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)