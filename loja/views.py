from django.shortcuts import render
from .models import Produto, Servico

# Create your views here.

def index(request):
    return render(request, "index.html")

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos.html", {"produtos": produtos})

def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, "servicos.html", {"servicos": servicos})
