from django.db import models

# Create your models here.
class User(models.Model):
    ingrediente = models.CharField()
    receita = models.CharField()