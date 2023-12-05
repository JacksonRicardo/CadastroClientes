# forms.py

from django import forms
from .models import Cliente, Funcionario, Gerente

class GerenteForm(forms.ModelForm):
    class Meta:
        model = Gerente
        fields = ['nome']

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'apelido', 'snap', 'cpf', 'gerente']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'telefone', 'cpf', 'funcionario']
