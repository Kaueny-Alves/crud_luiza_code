from django.forms import ModelForm, fields
from app.models import Empresas, Pacotes

class EmpresasForm(ModelForm):
  class Meta:
    model = Empresas
    fields = ['cnpj', 'nome', 'email', 'senha', 'telefone']
    
class PacotesForm(ModelForm):
  class Meta:
    model = Pacotes
    fields = ['preco', 'destino', 'quantidade', 'data', 'tipo', 'empresa']