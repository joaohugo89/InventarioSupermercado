from django import forms
from usuarios.models import *


class PessoaForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(PessoaForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = Pessoa
        fields = [
            "nome", "cpf", "email", "status", "password"
        ]

class GerenteForm(forms.ModelForm):

    class Meta:
        model = Gerente
        fields = ('__all__')

class VendedorForm(forms.ModelForm):

    class Meta:
        model = Vendedor
        fields = ('__all__')