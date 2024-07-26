from django.shortcuts import render, redirect
from usuarios.models import *
from usuarios.forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def cadastrar_pessoa(request):
    form = PessoaForm()
    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cadastrar_pessoa")
    return render(request, "usuarios/cadastrarusuarios.html", {"nome_pagina": "Cadastrar usuário","form": form})

# @login_required
def cadastrar_gerente(request):
    form = GerenteForm()
    if request.method == "POST":
        form = GerenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cadastrar_pessoa")
    return render(request, "usuarios/cadastrargerente.html", {"nome_pagina": "Cadastrar gerente", "form": form})

def cadastrar_vendedor(request):

    form = VendedorForm()

    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request, "usuarios/cadastrarvendedor.html", {"nome_pagina": "Cadastrar Vendedor", "form": form})

