from django import forms
from .models import Cliente, Funcionario

class ClienteForm(forms.ModelForm):
    # Adiciona um campo para selecionar o funcionário no formulário
    funcionario = forms.ModelChoiceField(queryset=Funcionario.objects.all(), required=False)  # Este campo é opcional

    class Meta:
        model = Cliente
        fields = ('nome', 'endereco', 'telefone', 'cpf', 'funcionario')  # Adiciona o campo funcionario ao formulário

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome', 'apelido', 'snap', 'cpf')
