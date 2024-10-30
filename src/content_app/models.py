from django.db import models
from django.contrib.auth.models import User

from datetime import date
from typing import List

class Content(models.Model):
    CONTENT_TYPES = [
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    file_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    upload_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True)
    status = models.CharField(max_length=20, default='published')
    creator = models.ForeignKey(User, related_name='contents', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Membro:
    def __init__(self, id: int, nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.referencias = []  # Lista de referências feitas pelo membro
        self.feedbacks = []    # Lista de feedbacks fornecidos pelo membro

class Plataforma:
    def __init__(self, id: int, nome: str, categoria: str):
        self.id = id
        self.nome = nome
        self.categoria = categoria

class Feedback:
    def __init__(self, id: int, cliente: Membro, plataforma: Plataforma, comentario: str, data: date):
        self.id = id
        self.cliente = cliente
        self.plataforma = plataforma
        self.comentario = comentario
        self.data = data

class Relatorio:
    def __init__(self, id: int, feedbacks: List[Feedback]):
        self.id = id
        self.feedbacks = feedbacks

    def gerar_relatorio(self):
        return f"Relatório {self.id} com {len(self.feedbacks)} feedbacks."

class Administrador:
    def __init__(self, id: int, nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email

class Referencia:
    def __init__(self, id: int, membro_referenciador: Membro, membro_referenciado: Membro, status: str):
        self.id = id
        self.membro_referenciador = membro_referenciador
        self.membro_referenciado = membro_referenciado
        self.status = status  # Exemplo: "pendente", "aprovada"

class Recompensa:
    def __init__(self, id: int, tipo: str, valor: float):
        self.id = id
        self.tipo = tipo
        self.valor = valor

class Sistema:
    def __init__(self):
        self.feedbacks = []
        self.referencias = []
        self.recompensas = []

    # Funções de feedback
    def registrar_feedback(self, cliente: Membro, feedback: Feedback):
        cliente.feedbacks.append(feedback)
        self.feedbacks.append(feedback)
        print(f"Feedback registrado para o cliente {cliente.nome}")

    def visualizar_feedback(self) -> List[Feedback]:
        return self.feedbacks

    def analisar_feedback(self) -> Relatorio:
        relatorio = Relatorio(id=1, feedbacks=self.feedbacks)
        return relatorio

    # Funções de referência e recompensa
    def registrar_referencia(self, membro: Membro, referencia: Referencia):
        membro.referencias.append(referencia)
        self.referencias.append(referencia)
        print(f"Referência registrada: {membro.nome} referenciou {referencia.membro_referenciado.nome}")

    def validar_referencia(self, referencia: Referencia):
        referencia.status = "aprovada"
        print(f"Referência {referencia.id} aprovada para {referencia.membro_referenciado.nome}")

    def conceder_recompensa(self, membro: Membro, recompensa: Recompensa):
        self.recompensas.append(recompensa)
        print(f"Recompensa concedida a {membro.nome}: {recompensa.tipo} no valor de {recompensa.valor}")