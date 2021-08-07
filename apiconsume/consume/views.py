import requests
from django.shortcuts import render

def clientes_cadastrados(request):
    queryset = requests.get("http://127.0.0.1:8000/api/v1/clientes/", headers={"Authorization" : "Token 0c480b96bb2f9d662394c95eb5d71c6f23124951"}).json()
    return render(request, "clientes_cadastrados.html", {'queryset' : queryset})

def garagens_ativas(request):
    queryset = requests.get("http://127.0.0.1:8000/api/v1/garagem/", headers={"Authorization" : "Token 0c480b96bb2f9d662394c95eb5d71c6f23124951"}).json()
    return render(request, "garagens_ativas.html", {'queryset' : queryset})

def clientes_carro(request):
    queryset = requests.get("http://127.0.0.1:8000/api/v1/clientes/car", headers={"Authorization" : "Token 0c480b96bb2f9d662394c95eb5d71c6f23124951"}).json()
    return render(request, "clientes_carro.html", {'queryset' : queryset})

def clientes_sem_carro(request):
    queryset = requests.get("http://127.0.0.1:8000/api/v1/clientes/nocar", headers={"Authorization" : "Token 0c480b96bb2f9d662394c95eb5d71c6f23124951"}).json()
    return render(request, "clientes_sem_carro.html", {'queryset' : queryset})


