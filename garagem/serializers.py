from rest_framework import serializers
from .models import Garagem, Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('name',)
 
class CarSerializer(serializers.ModelSerializer):
    class Meta:
         model = Vehicle
         fields = ('name','color', 'year',)

class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('name', 'model', 'year',)

class GaragemSerializerGet(serializers.ModelSerializer):

    vehicle = VehicleSerializer(read_only=True, many=True)

    class Meta:
        fields = ('email','phone','vehicle')
        model = Garagem

class GaragemSerializerPost(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Garagem
class VehicleRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Vehicle