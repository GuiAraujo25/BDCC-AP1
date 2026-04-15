from rest_framework import serializers
from .models import Produto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    # Isso faz aparecer o nome da categoria no JSON da API
    categoria_detalhes = CategoriaSerializer(source='categoria', read_only=True)

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricaao', 'preco', 'imagem', 'data_criacao', 'categoria', 'categoria_detalhes']