from django.contrib import admin
from usuarios.models import *

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Gerente)
admin.site.register(Vendedor)