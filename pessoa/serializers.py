from rest_framework import serializers
from .models import PersonCustomer
from garagem.models import Garagem, Vehicle

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonCustomer
        fields = ('id','name',)

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('name',)

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonCustomer
        fields = ('id','name','email','phone')

class PessoaSerializerCar(serializers.ModelSerializer):
    person = CustomerSerializer(read_only=True)
    vehicle = VehicleSerializer(read_only=True, many=True)
    class Meta:
        fields = ('person','vehicle')
        model = Garagem
