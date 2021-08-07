from . import views
from django.urls import path

urlpatterns = [
    path('api/clientes', views.clientes_cadastrados),
    path('api/garagem', views.garagens_ativas),
    path('api/clientes/car', views.clientes_carro),
    path('api/clientes/nocar', views.clientes_sem_carro),
]