from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"CPF":"CPF invalido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({"NOME":"Não inclua numeros no nome."})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"RG":"O rg deve ter 9 digitos."})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"celular":"O celular estar no modelo: 11 91234-4321"})
        return data
    