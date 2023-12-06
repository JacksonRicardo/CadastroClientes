from django.db import models

class Gerente(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")    
    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    empresa = models.CharField(max_length=255, verbose_name="Empresa", null=True)
    instagram = models.CharField(max_length=255, verbose_name="Instagram", null=True)
    cpf = models.CharField(max_length=255, verbose_name="CPF")
    gerente = models.ForeignKey(Gerente, on_delete=models.SET_NULL, null=True, blank=True, related_name='funcionarios', verbose_name="Gerente")
    
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    endereco = models.CharField(max_length=350, verbose_name="Endereço")
    telefone = models.CharField(max_length=255, verbose_name="Telefone")
    cpf = models.CharField(max_length=255, verbose_name="CPF")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True, related_name='clientes', verbose_name="Funcionário que atende")
    
    def __str__(self):
        return self.nome
