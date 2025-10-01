from .models import Ingrediente, Receita

def seed():
    ing_nomes = ["Tomate", "Cebola", "Alface", "Queijo", "Pão", "Presunto", "Peito de frango", "Maionese"]
    ingredientes = {}
    for nome in ing_nomes:
        ingredientes[nome] = Ingrediente.objects.get_or_create(nome=nome)[0]

    # receita 1
    r1 = Receita.objects.create(titulo="Sanduíche Simples")
    r1.ingredientes.set([ingredientes["Pão"], ingredientes["Queijo"], ingredientes["Presunto"]])

    # receita 2
    r2 = Receita.objects.create(titulo="Salada Verde")
    r2.ingredientes.set([ingredientes["Alface"], ingredientes["Tomate"], ingredientes["Cebola"]])

    # receita 3
    r3 = Receita.objects.create(titulo="Sanduíche de Frango")
    r3.ingredientes.set([ingredientes["Pão"], ingredientes["Peito de frango"], ingredientes["Maionese"]])
