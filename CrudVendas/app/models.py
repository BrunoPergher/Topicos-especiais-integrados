from django.db import models

# Create your models here.

class User(models.Model):
  nome = models.CharField(max_length=100)
  idade = models.IntegerField()
  cpf = models.CharField(max_length=100)
  isVendedor = models.BooleanField(default=False)

class Produto(models.Model):
  nome = models.CharField(max_length=100)
  descricao = models.CharField(max_length=100)
  valor = models.IntegerField()
  estoque = models.IntegerField()

class Venda(models.Model):
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='venda_cliente')
  cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='venda_vendedor')
  quantidade = models.IntegerField()