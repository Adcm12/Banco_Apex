from rest_framework import serializers
from Banco.models import Conta_Corriente, Conta_poupança


class CorrienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta_Corriente
        fields = '__all__'


class PoupançaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta_poupança
        fields = '__all__'
