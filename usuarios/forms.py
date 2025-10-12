from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Endereco


class RegisterForm(UserCreationForm):
    rua = forms.CharField(max_length=100, required=True)
    numero = forms.CharField(max_length=10, required=True)
    cidade = forms.CharField(max_length=50, required=True)
    estado = forms.CharField(max_length=50, required=True)
    cep = forms.CharField(max_length=8, required=True)

    class Meta:
        model = Usuario
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "cpf",
            "telefone",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        """Salva o usuário e cria o endereço vinculado."""
        user = super().save(commit=False)
        if commit:
            user.save()
            endereco = Endereco.objects.create(
                rua=self.cleaned_data["rua"],
                numero=self.cleaned_data["numero"],
                cidade=self.cleaned_data["cidade"],
                estado=self.cleaned_data["estado"],
                cep=self.cleaned_data["cep"],
            )
            user.endereco = endereco
            user.save()
        return user
