from django.forms import ModelForm, fields
from app.models import Empresas

class EmpresasForm(ModelForm):
  class Meta:
    model = Empresas
    fields = ['cnpj', 'nome', 'email', 'senha', 'telefone']