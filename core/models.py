from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    total_cotas = models.PositiveIntegerField()
    valor_cota = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Cota(models.Model):
    STATUS_CHOICES = (
        ('livre', 'Livre'),
        ('reservada', 'Reservada'),
        ('paga', 'Paga'),
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    numero_cota = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='livre')

    class Meta:
        unique_together = ('produto', 'numero_cota')

    def __str__(self):
        return f'Cota {self.numero_cota} - {self.status}'

class Sorteio(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    numero_sorteado = models.PositiveIntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Sorteio do produto {self.produto.nome} - Ganhador: {self.usuario.username}'
