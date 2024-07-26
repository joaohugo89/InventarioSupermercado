from django.urls import path

from . import views

urlpatterns = [
    path('Compra-produtos/', views.compra_de_produtos, name="compra_de_produtos"),
    path('Venda-de-produtos/', views.venda_de_produtos, name="venda_de_produtos"),
    path('Relatorio-movimentações/', views.relatorio_movimentacoes, name="relatorio_movimentacoes",),
]