from django.shortcuts import render, redirect
from .models import Produto, Cota, Sorteio
from django.contrib.auth.decorators import login_required
import random
from django.contrib import messages

def home(request):
    produtos = Produto.objects.filter(ativo=True)
    return render(request, 'home.html', {'produtos': produtos})

def produto_detail(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    cotas = Cota.objects.filter(produto=produto).order_by('numero_cota')
    return render(request, 'produto_detail.html', {'produto': produto, 'cotas': cotas})

@login_required
def sortear(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    cotas_pagas = Cota.objects.filter(produto=produto, status='paga')
    if cotas_pagas.exists():
        cota_ganhadora = random.choice(list(cotas_pagas))
        Sorteio.objects.create(
            produto=produto,
            numero_sorteado=cota_ganhadora.numero_cota,
            usuario=cota_ganhadora.usuario
        )
        messages.success(request, f'Sorteio realizado! Ganhador: {cota_ganhadora.usuario.username}')
    else:
        messages.error(request, 'Nenhuma cota paga para realizar o sorteio.')
    return redirect('produto_detail', produto_id=produto.id)
