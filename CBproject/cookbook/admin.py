from django.contrib import admin
from .models import Ingrediente, Receita

admin.site.register(Ingrediente)

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    filter_horizontal = ('ingredientes',)

from cookbook.models import Ingrediente, Receita

farinha = Ingrediente.objects.create(nome="Farinha", quantidade="2 xícaras")
ovo = Ingrediente.objects.create(nome="Ovo", quantidade="3 unidades")
leite = Ingrediente.objects.create(nome="Leite", quantidade="1 copo")

bolo = Receita.objects.create(titulo="Bolo Simples", descricao="Misture tudo e asse.")
bolo.ingredientes.add(farinha, ovo, leite)