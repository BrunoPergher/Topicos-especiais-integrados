from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=100)
    isVendedor = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    valor = models.IntegerField()
    estoque = models.IntegerField()
  
    def __str__(self):
        return self.nome

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    # Adicione limit_choices_to para mostrar apenas vendedores
    vendedor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='venda_cliente',
        limit_choices_to={'isVendedor': True}  # Filtre apenas os vendedores
    )

    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='venda_vendedor')
    quantidade = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.quantidade <= self.produto.estoque:
            self.produto.estoque -= self.quantidade
            self.produto.save()
            super(Venda, self).save(*args, **kwargs)
        else:
            raise ValueError("Quantidade de produto excede o estoque disponível")
