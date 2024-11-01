from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Membro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='feedbacks')
    comentario = models.TextField()
    data = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.membro.user.username} - {self.comentario[:20]}"

class Relatorio(models.Model):
    feedbacks = models.ManyToManyField(Feedback)
    
    def gerar_relatorio(self):
        return f"Relatório contendo {self.feedbacks.count()} feedback(s)."
