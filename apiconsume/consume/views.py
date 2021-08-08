from django.shortcuts import render
import requests

def clientes_cadastrados(request):
    queryset = requests.get("http://127.0.0.1:8000/api/v1/clientes/", headers={"Authorization" : "Token bcba1f9a392c5dedc7070f806dd55410ca5fef09"}).json()
    return render(request, "clientes_cadastrados.html", {'queryset' : queryset})

def garagens_ativas(request):
    queryset = requests.get("http://127.0.0.1:8000/api/v1/garagem/", headers={"Authorization" : "Token bcba1f9a392c5dedc7070f806dd55410ca5fef09"}).json()
    return render(request, "garagens_ativas.html", {'queryset' : queryset})

def clientes_carro(request):
    queryset = requests.get("http://127.0.0.1:8000/api/v1/clientes/car", headers={"Authorization" : "Token bcba1f9a392c5dedc7070f806dd55410ca5fef09"}).json()
    return render(request, "clientes_carro.html", {'queryset' : queryset})

def clientes_sem_carro(request):
    queryset = requests.get("http://127.0.0.1:8000/api/v1/clientes/nocar", headers={"Authorization" : "Token bcba1f9a392c5dedc7070f806dd55410ca5fef09"}).json()
    return render(request, "clientes_sem_carro.html", {'queryset' : queryset})


