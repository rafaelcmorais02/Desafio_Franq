from django.urls import path
from .views import CreatePerson, ManagePerson, ListClient, ListClientCar, ListClientNoCar
urlpatterns = [
    path('pessoa/cadastrar', CreatePerson.as_view()),
    path('pessoa/atualizar/<int:pk>/', ManagePerson.as_view()),
    path('clientes/', ListClient.as_view()),
    path('clientes/nocar', ListClientNoCar.as_view()),
    path('clientes/car', ListClientCar.as_view()),
]
