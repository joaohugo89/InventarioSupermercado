from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('cadastrar_gerente/', views.cadastrar_gerente, name='cadastrar_gerente'),
    path('cadastrar_vendedor/', views.cadastrar_vendedor, name='cadastrar_vendedor'),
    path("logout/", auth_views.LogoutView.as_view(template_name="usuarios/logout.html"), name="logout"),
    path("login/", auth_views.LoginView.as_view(template_name="usuarios/login.html"), name="login"),
]