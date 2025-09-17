from django.contrib import admin
from .models import Produto, Servico

# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "estoque")
    search_fields = ("nome",)


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "preco_base")
    search_fields = ("titulo",)
