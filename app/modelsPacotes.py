from app.models import Empresas
from django.db import models

class Pacotes(models.Model):
    TIPO_CHOICES=(
    ('N', 'Nacional'),
    ('I', 'Internacional'),
)
    preco = models.CharField(max_length=10)
    destino = models.CharField(max_length=100)
    data = models.CharField(max_length=10)
    tipo = models.CharField(max_length=1,choices=TIPO_CHOICES)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)

