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
        self.convites = []
        self.feedbacks = []
        self.recompensas = []

class Feedback:
    def __init__(self, id: int, membro: Membro, comentario: str, data: date):
        self.id = id
        self.membro = membro
        self.comentario = comentario
        self.data = data

class Relatorio:
    def __init__(self, feedbacks: List[Feedback]):
        self.feedbacks = feedbacks

    def gerar_relatorio(self):
        return f"Relatório com {len(self.feedbacks)} feedbacks."

class Administrador:
    def __init__(self, id: int, nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email

class Convite:
    def __init__(self, convidador: Membro, convidado: Membro, status: str):
        self.convidador = convidador
        self.convidado = convidado
        self.status = status

class Recompensa:
    def __init__(self, tipo: str, valor: float):
        self.tipo = tipo
        self.valor = valor

class Sistema:
    def __init__(self):
        self.feedbacks = []
        self.convites = []
        self.recompensas = []

    def registrar_feedback(self, membro: Membro, feedback: Feedback):
        membro.feedbacks.append(feedback)
        self.feedbacks.append(feedback)
        print(f"Feedback registrado para o membro {membro.nome}")

    def visualizar_feedback(self) -> List[Feedback]:
        return self.feedbacks

    def analisar_feedback(self) -> Relatorio:
        relatorio = Relatorio(feedbacks=self.feedbacks)
        return relatorio

    def registrar_convite(self, membro: Membro, convite: Convite):
        membro.convites.append(convite)
        self.convites.append(convite)
        print(f"Convite registrado: {membro.nome} convidou {convite.convidado.nome}")

    def validar_convite(self, convite: Convite):
        convite.status = "aprovado"
        print(f"Convite aprovado para {convite.convidado.nome}")

    def conceder_recompensa(self, membro: Membro, recompensa: Recompensa):
        membro.recompensas.append(recompensa)
        self.recompensas.append(recompensa)
        print(f"Recompensa concedida a {membro.nome}: {recompensa.tipo} no valor de {recompensa.valor}")
