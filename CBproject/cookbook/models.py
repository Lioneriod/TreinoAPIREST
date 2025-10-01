from django.db import models

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.titulo
