from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

cpf_validator = RegexValidator(r'^\d{11}$')


class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{8}$')])

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, validators=[cpf_validator], blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.username
