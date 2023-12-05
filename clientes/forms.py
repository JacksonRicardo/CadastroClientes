from django import forms
from .models import Cliente, Funcionario

class ClienteForm(forms.ModelForm):
    funcionario = forms.ModelChoiceField(queryset=Funcionario.objects.all(), required=False)  

    class Meta:
        model = Cliente
        fields = ('nome', 'endereco', 'telefone', 'cpf', 'funcionario')

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome', 'apelido', 'snap', 'cpf')
