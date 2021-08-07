from django.urls import path
from .views import GetList, GetVehicleDetail, GetAtive, PutList
urlpatterns = [
    path('garagem/', GetAtive.as_view()),
    path('garagem/<int:pk>/', GetList.as_view()),
    path('garagem/atualizar/<int:pk>/', PutList.as_view()),
    path('veiculo/<int:pk>/', GetVehicleDetail.as_view())
]
