from rest_framework import generics, permissions
from .models import Garagem, Vehicle
from .serializers import GaragemSerializerGet, GaragemSerializerPost, CarSerializer, MotoSerializer, VehicleRegisterSerializer

class GetList(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Garagem.objects.all()
    serializer_class = GaragemSerializerGet    

class PutList(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Garagem.objects.all()
    serializer_class = GaragemSerializerPost

class GetVehicleDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Vehicle.objects.all()
    def get_serializer_class(self):
            pk= self.kwargs.get('pk')
            obj = Vehicle.objects.get(id=pk)
            field_value = getattr(obj, 'category')
            if(field_value == "C"):
                serializer_class = CarSerializer
            elif (field_value == "M"):
                serializer_class = MotoSerializer
            return serializer_class

class GetAtive(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Garagem.objects.exclude(vehicle__isnull = True)
    serializer_class = GaragemSerializerGet

class VehicleRegister(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Vehicle.objects.all()
    serializer_class = VehicleRegisterSerializer


    
   
