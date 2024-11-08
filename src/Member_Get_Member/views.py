from django.shortcuts import render
from rest_framework import viewsets
from .models import Convite, Recompensa, Sistema
from .serializers import ConviteSerializer, RecompensaSerializer, SistemaSerializer

class ConviteViewSet(viewsets.ModelViewSet):
    queryset = Convite.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ConviteSerializer  # Use o serializer que mostra apenas o email
        return ConviteSerializer  # Para outras ações, use o serializer completo

class RecompensaViewSet(viewsets.ModelViewSet):
    queryset = Recompensa.objects.all()
    serializer_class = RecompensaSerializer

class SistemaViewSet(viewsets.ModelViewSet):
    queryset = Sistema.objects.all()
    serializer_class = SistemaSerializer
