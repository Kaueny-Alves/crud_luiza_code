from django.db import models

class Empresas(models.Model):
    cnpj = models.CharField(max_length=14)
    nome = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    
class Pacotes(models.Model):
    TIPO_CHOICES=(
    ('N', 'Nacional'),
    ('I', 'Internacional'),
)
    preco = models.CharField(max_length=10)
    destino = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=10)
    data = models.CharField(max_length=10)
    tipo = models.CharField(max_length=1,choices=TIPO_CHOICES)
    empresa = models.CharField(max_length=100, default="")
    