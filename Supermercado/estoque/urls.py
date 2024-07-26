from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produto_estoque/', views.produto_estoque, name='produto_estoque'),
    path('listar_produto/', views.listar_produto, name='listar_produto'),
    path('produtos_cadastrados/', views.produtos_cadastrados, name='produtos_cadastrados'),
]