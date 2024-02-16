from django.http import JsonResponse
from rest_framework import viewsets
from Banco.models import Conta_poupança, Conta_Corriente
from .serializer import CorrienteSerializer, PoupançaSerializer

    
class CorrienteViewSets(viewsets.ModelViewSet):
    "Exibindo todos os Cursos"
    queryset = Conta_Corriente.objects.all()
    serializer_class = CorrienteSerializer

class PoupançaViewSets(viewsets.ModelViewSet):
    "Exibindo todos os Cursos"
    queryset = Conta_poupança.objects.all()
    serializer_class = PoupançaSerializer