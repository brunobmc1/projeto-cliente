from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "Número de CPF inválido"})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua números neste campo"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O rg deve ter 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O celular deve ser no formato: 11 91234-1234"})
        return data
    



    # def validate_nome(self, nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError("Não inclua números neste campo")
    #     return nome
    # def validate_rg(self, rg):
    #     if len(rg) != 9:
    #         raise serializers.ValidationError("O rg deve ter 9 dígitos")
    #     return rg
    # def validate_celular(self,celular):
    #     if len(celular) < 11:
    #         raise serializers.ValidationError("O celular deve ter 11 dígitos")
    #     return celular