from django.http import JsonResponse
from rest_framework import viewsets
from Banco.models import Conta_poupança, Conta_Corriente
from .serializer import CorrienteSerializer, PoupançaSerializer

# Create your views here.

def conta_corriente(request):
    if request.method == 'GET':
        conta = {'Id': 1, 'Nome': 'Seu Nome'}
        return JsonResponse(conta)
    
def conta_poupança(request):
    if request.method == 'GET':
        conta = {'Id': 1, 'Nome': 'Seu Nome'}
        return JsonResponse(conta)
    
class CorrienteViewSets(viewsets.ModelViewSet):
    "Exibindo todos os Cursos"
    queryset = Conta_Corriente.objects.all()
    serializer_class = CorrienteSerializer




class PoupançaViewSets(viewsets.ModelViewSet):
    "Exibindo todos os Cursos"
    queryset = Conta_poupança.objects.all()
    serializer_class = PoupançaSerializer