from rest_framework import serializers
from .models import Convite, Recompensa, Sistema
from django.utils import timezone

class ConviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convite
        fields = ['convidado_email']  #Exibe apenas o email na API
        extra_kwargs = {
            'data_criacao': {'read_only': True},  # Define como somente leitura
            'data_expiracao': {'read_only': True},  # Define como somente leitura
            'status': {'read_only': True},  # Define como somente leitura
            'limite': {'read_only': True},  # Define como somente leitura
            'convidador': {'read_only': True},  # Define como somente leitura
        }

    def create(self, validated_data):
        validated_data['data_criacao'] = timezone.now()
        validated_data['data_expiracao'] = timezone.now() + timezone.timedelta(days=30)
        validated_data['status'] = 'pendente'  # Define um valor padrão para status
        validated_data['convidador'] = self.context['request'].user.membro 
        
        return super().create(validated_data)

class RecompensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recompensa
        fields = '__all__'

class SistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sistema
        fields = '__all__'
