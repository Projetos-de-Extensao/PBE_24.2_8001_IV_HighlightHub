from django.shortcuts import render

# Create your views here.
# views.py in Member_Get_Member

from rest_framework import viewsets
from .models import Convite, Recompensa, Sistema
from .serializers import ConviteSerializer, RecompensaSerializer, SistemaSerializer

class ConviteViewSet(viewsets.ModelViewSet):
    queryset = Convite.objects.all()
    serializer_class = ConviteSerializer

class RecompensaViewSet(viewsets.ModelViewSet):
    queryset = Recompensa.objects.all()
    serializer_class = RecompensaSerializer

class SistemaViewSet(viewsets.ModelViewSet):
    queryset = Sistema.objects.all()
    serializer_class = SistemaSerializer
