from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    apelido = models.CharField(max_length=255, verbose_name="Apelido")
    snap = models.CharField(max_length=255, verbose_name="Snap")
    cpf = models.CharField(max_length=255, verbose_name="CPF")
    
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    endereco = models.CharField(max_length=350, verbose_name="Endereço")
    telefone = models.CharField(max_length=255, verbose_name="Telefone")
    cpf = models.CharField(max_length=255, verbose_name="CPF")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Funcionário que atende")

