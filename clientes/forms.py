# forms.py

from django import forms
from .models import Cliente, Funcionario, Gerente

class GerenteForm(forms.ModelForm):
    class Meta:
        model = Gerente
        fields = ['nome']

class FuncionarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gerente'].widget.attrs['class'] = 'custom-select'

    gerente = forms.ModelChoiceField(queryset=Gerente.objects.all(), required=False)

    class Meta:
            model = Funcionario
            fields = ['nome', 'apelido', 'snap', 'cpf', 'gerente']
class ClienteForm(forms.ModelForm):
    funcionario = forms.ModelChoiceField(queryset=Funcionario.objects.all(), required=False)
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'telefone', 'cpf', 'funcionario']
