from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def conta_corriente(request):
    if request.method == 'GET':
        conta = {'Id': 1, 'Nome': 'Seu Nome'}
        return JsonResponse(conta)
    
def conta_poupança(request):
    if request.method == 'GET':
        conta = {'Id': 1, 'Nome': 'Seu Nome'}
        return JsonResponse(conta)