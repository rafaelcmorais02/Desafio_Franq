from .models import PersonCustomer
from rest_framework import generics,permissions
from .serializers import PessoaSerializer, PessoaSerializerCar
from garagem.models import Garagem

class CreatePerson(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = PersonCustomer.objects.all()
    serializer_class = PessoaSerializer

class ManagePerson(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = PersonCustomer.objects.all()
    serializer_class = PessoaSerializer

class ListClient(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = PersonCustomer.objects.all()
    serializer_class = PessoaSerializer

class ListClientNoCar(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Garagem.objects.filter(vehicle__isnull = True)
    serializer_class = PessoaSerializerCar

class ListClientCar(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Garagem.objects.exclude(vehicle__isnull = True)
    serializer_class = PessoaSerializerCar