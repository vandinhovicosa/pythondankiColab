from django.db import models

# Create your models here.
from Enderecos.models import Endereco
from Pessoa.models import Pessoa


class Cadastro_Produtos(models.Model):
    foto = models.ImageField(upload_to='fotodpesoal', null=True, blank=True)
    produto = models.CharField(max_length=255, null=False, blank=False)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    data_pedido = models.DateField(null=False, blank=False)
    descricao = models.FileField(upload_to='descricao/', null=True, blank=True)
    relatorio = models.FileField(upload_to='relatorios/', null=True, blank=True)
    obs = models.TextField()
    endereco_entrega = models.ForeignKey(Endereco, blank=False, null=False, on_delete=models.CASCADE)
    outro_remetente = models.ManyToManyField(Pessoa, blank=True)

    def __str__(self):
        return self.produto
