from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cliente, Funcionario, Gerente
from .forms import ClienteForm, FuncionarioForm, GerenteForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    clientes = Cliente.objects.all()
    funcionarios = Funcionario.objects.all()
    gerentes = Gerente.objects.all()
    contexto = {
        'clientes': clientes,
        'funcionarios': funcionarios,
        'gerentes': gerentes,   
    }
    resposta = render(request, template_name="clientes/home.html", context=contexto)
    return HttpResponse(resposta)

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/cliente_form.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        funcionario_id = self.request.POST.get('funcionario_id')
        if funcionario_id:
            funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
            cliente = form.save(commit=False)
            cliente.funcionario = funcionario
            cliente.save()

        return super().form_valid(form)

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/cliente_form.html"
    success_url = reverse_lazy('home')

def detalhes_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    funcionario_atende = cliente.funcionario  # Obter o funcionário que atende este cliente, se existir
    contexto = {
        'cliente': cliente,
        'funcionario_atende': funcionario_atende,  # Adicionar o funcionário que atende este cliente ao contexto
    }
    return render(request, template_name="clientes/cliente.html", context=contexto)
    
def deleta_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('home') 

class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = "funcionarios/funcionario_form.html"
    success_url = reverse_lazy('home')

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = "funcionarios/funcionario_form.html"
    success_url = reverse_lazy('home')

def detalhes_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    clientes_atendidos = Cliente.objects.filter(funcionario=funcionario)  # Obter clientes atendidos por este funcionário
    contexto = {
        'funcionario': funcionario,
        'clientes_atendidos': clientes_atendidos,  # Adicionar os clientes atendidos por este funcionário ao contexto
    }
    return render(request, template_name="funcionarios/funcionario.html", context=contexto)

def detalhes_gerente(request, pk):
    gerente = get_object_or_404(Gerente, pk=pk)
    funcionarios = Funcionario.objects.filter(gerente=gerente)  # Obtém os funcionários gerenciados por este gerente
    contexto = {
        'gerente': gerente,
        'funcionarios': funcionarios,  # Adiciona os funcionários gerenciados por este gerente ao contexto
    }
    return render(request, template_name="gerentes/gerente.html", context=contexto)


def deleta_funcionario(request, pk):
    funcionario = Funcionario.objects.get(pk=pk)
    funcionario.delete()
    return redirect('home')  

class GerenteUpdateView(UpdateView):
    model = Gerente
    form_class = GerenteForm
    template_name = "gerentes/gerente_form.html"
    success_url = reverse_lazy('home')  

class GerenteCreateView(CreateView):
    model = Gerente
    fields = ['nome']
    template_name = "gerentes/gerente_create.html"
    success_url = reverse_lazy('home')
    
from django.contrib.auth import authenticate, login

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})





