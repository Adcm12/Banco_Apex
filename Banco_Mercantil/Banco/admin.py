
from django.contrib import admin
from Banco.models import Conta_Corriente, Conta_poupança

class Conta_corriente_admin(admin.ModelAdmin):
    list_display = ('id', 'conta', 'tipo_conta', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Conta_Corriente, Conta_corriente_admin)

class Conta_Poupança_admin(admin.ModelAdmin):
    list_display = ('id', 'conta', 'tipo_conta', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Conta_poupança, Conta_Poupança_admin)