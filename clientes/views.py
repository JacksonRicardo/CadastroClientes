from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cliente, Funcionario
from .forms import ClienteForm, FuncionarioForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

def home(request):
    clientes = Cliente.objects.all()
    funcionarios = Funcionario.objects.all()
    contexto = {
        'clientes': clientes,
        'funcionarios': funcionarios,      
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


def deleta_funcionario(request, pk):
    funcionario = Funcionario.objects.get(pk=pk)
    funcionario.delete()
    return redirect('home')  
