from rest_framework import serializers
from .models import Ingrediente, Receita

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nome']

class ReceitaSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True)

    class Meta:
        model = Receita
        fields = ['id', 'titulo', 'ingredientes']

    def create(self, validated_data):
        ingredientes_data = validated_data.pop('ingredientes')
        receita = Receita.objects.create(**validated_data)
        for ingr in ingredientes_data:
            ingrediente_obj, created = Ingrediente.objects.get_or_create(**ingr)
            receita.ingredientes.add(ingrediente_obj)
        return receita

    def update(self, instance, validated_data):
        ingredientes_data = validated_data.pop('ingredientes', None)
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.save()

        if ingredientes_data is not None:
            # aqui usamos set para garantir que relações antigas sejam removidas
            new_ingredientes = []
            for ingr in ingredientes_data:
                ingrediente_obj, created = Ingrediente.objects.get_or_create(**ingr)
                new_ingredientes.append(ingrediente_obj)
            instance.ingredientes.set(new_ingredientes)

        return instance

