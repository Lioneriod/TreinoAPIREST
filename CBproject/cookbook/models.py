from django.db import models

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)  # <-- permite vazio
    ingredientes = models.ManyToManyField(Ingrediente, through="ReceitaIngrediente")


class ReceitaIngrediente(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('receita', 'ingrediente')


def __str__(self):
    return f"{self.receita.titulo} - {self.ingrediente.nome}"

