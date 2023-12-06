# forms.py
from django import forms
from django.shortcuts import redirect, render
from .models import Cliente, Funcionario, Gerente
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login 

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

def tela_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirecionar para a página desejada após o login
                return redirect('home')  # Altere 'home' para sua página inicial
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})