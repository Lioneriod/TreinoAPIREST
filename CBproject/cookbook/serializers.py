from rest_framework import serializers
from .models import Ingrediente, Receita

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nome', 'quantidade']

class ReceitaSerializer(serializers.ModelSerializer):

    ingredientes = IngredienteSerializer(many=True, read_only=True)
    
    ingredientes_ids = serializers.PrimaryKeyRelatedField(
        queryset=Ingrediente.objects.all(),
        many=True,
        write_only=True,
        source='ingredientes'
    )

    class Meta:
        model = Receita
        fields = ['id', 'titulo', 'descricao', 'ingredientes', 'ingredientes_ids']
