from rest_framework import serializers
from .models import Cliente
from .validators import (
    cpf_valido,
    nome_valido,
    rg_valido,
    rg_so_numeros,
    celular_valido
)


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    

    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O campo nome não pode conter números'})
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'CPF inválido'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve conter 9 dígitos'})
        if not rg_so_numeros(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve conter apenas dígitos'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O celular deve conter 11 dígitos numéricos no modelo 00 00000-0000'})

        return data

