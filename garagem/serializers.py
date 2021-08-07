from rest_framework import serializers
from .models import Garagem, Vehicle
from pessoa.models import PersonCustumer

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('name',)
 
class CarSerializer(serializers.ModelSerializer):
    class Meta:
         model = Vehicle
         fields = ('name','color', 'year', 'category')

class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('name', 'model', 'year', 'category')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonCustumer
        fields = ('email', 'phone',)

class GaragemSerializerGet(serializers.ModelSerializer):

    person = PersonSerializer(read_only=True)
    vehicle = VehicleSerializer(read_only=True, many=True)

    class Meta:
        fields = ('person','vehicle')
        model = Garagem

class GaragemSerializerPost(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Garagem
