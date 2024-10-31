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
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email
        self.convites = []
        self.feedbacks = []
        self.recompensas = []

class Feedback:
    def __init__(self, id, membro: Membro, comentario, data: date):
        self.id = id
        self.membro = membro
        self.comentario = comentario
        self.data = data

class Relatorio:
    def __init__(self, feedbacks):
        self.feedbacks = feedbacks

    def gerar_relatorio(self):
        pass

class Administrador:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

class Convite:
    def __init__(self, convidador: Membro, convidado: Membro, status):
        self.convidador = convidador
        self.convidado = convidado
        self.status = status

class Recompensa:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class Sistema:
    def __init__(self):
        self.feedbacks = []
        self.convites = []
        self.recompensas = []

    def registrar_feedback(self, membro: Membro, feedback: Feedback):
        pass

    def visualizar_feedback(self):
        pass

    def analisar_feedback(self):
        pass

    def registrar_convite(self, membro: Membro, convite: Convite):
        pass

    def validar_convite(self, convite: Convite):
        pass

    def conceder_recompensa(self, membro: Membro, recompensa: Recompensa):
        pass
