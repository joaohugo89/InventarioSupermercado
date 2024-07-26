from django.shortcuts import render, redirect
from estoque.models import *
from estoque.forms import *
import datetime

# Create your views here.
def cadastrar_produto(request):
    form = ProdutoForm()
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cadastrar_produto")
    return render(request, "estoque/cadastrar_produto.html", {"nome_pagina": "Cadastrar produto", "form": form})

def produto_estoque(request):
    form = ProdutoEstoqueForm()
    if request.method == "POST":
        form = ProdutoEstoqueForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("produto_estoque")
    return render(request, "estoque/produto_estoque.html", {"nome_pagina": "Produto estoque", "form": form})


def listar_produto(request):
    allproduto = ProdutoEstoque.objects.all()
    if request.POST:
        pesquisa = request.POST.get("pesquisa", None)
        allproduto = ProdutoEstoque.objects.filter(
            produto__nome__contains=pesquisa)
    today = datetime.date.today()
    listProdutoEstoque = []
    for q in allproduto:
        if q.data_de_validade >= today:
            diasVenc = q.data_de_validade - today
            diasVenc = diasVenc.days
        else:
            diasVenc = 0
        obj = {
            'Produto': q,
            "DiasVenc": diasVenc,
        }
        listProdutoEstoque.append(obj)
    return render(request, "estoque/listar_produtos.html", {"listProdutoEstoque": listProdutoEstoque})

def produtos_cadastrados(request):
    allcadastro = Produto.objects.all()
    return render(request, "estoque/listar_produtos_cadastrados.html", {"listProduto": allcadastro})