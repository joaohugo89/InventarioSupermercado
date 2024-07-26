from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

# Create your models here.
STATUS_GENERO = [
    ("FEMININO", "Feminino"),
    ("MASCULINO", "Masculino"),
    ("OUTRO", "Outro"),
]

class UsuarioManager(BaseUserManager):

    def create_user(self, email, password=None):
        usuario = self.model(
            email=self.normalize_email(email),
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save()

        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()

        return usuario

class Pessoa(AbstractBaseUser, PermissionsMixin):

    nome = models.CharField(verbose_name="Nome completo:", max_length=194)

    status = models.CharField(verbose_name="Genero",
                              max_length=10, choices=STATUS_GENERO)
    email = models.EmailField(verbose_name="E-mail:",
                              unique=True, blank=False, null=False)
    cpf = models.CharField(verbose_name="CPF:", max_length=14,
                           unique=True, blank=False, null=False)
    data_de_cadastro = models.DateTimeField(
        verbose_name="Data do cadastro", auto_now_add=True)
    is_active = models.BooleanField(
        verbose_name="Usuário está ativo",
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento",
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name="Usuário é um superusuário",
        default=False,
    )

    USERNAME_FIELD = "email"

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        db_table = "pessoa"

    def __str__(self):
        return self.nome

class Gerente(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Gerente"
        verbose_name_plural = "Gerentes"
        db_table = "Gerente"

    def __str__(self):
        return self.pessoa.nome
    
class Vendedor(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        db_table = "vendedor"

    def __str__(self):
        return self.pessoa.nome