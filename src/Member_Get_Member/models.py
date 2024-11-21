from django.db import models
from django.utils import timezone
from Feedback.models import Membro, Feedback, Relatorio
import uuid

class Convite(models.Model):
    STATUS_CONVITE = [
        ('pendente', 'Pendente'),
        ('aceito', 'Aceito'),
        ('expirado', 'Expirado'),
    ]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=True)
    convidador = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='convites_enviados')
    convidado_email = models.EmailField(null=True) 
    status = models.CharField(max_length=20, choices=STATUS_CONVITE, default='pendente')
    data_criacao = models.DateTimeField(default=timezone.now)
    data_expiracao = models.DateTimeField()

    def __str__(self):
        return f"Convite de {self.convidador.user.username} para {self.convidado_email} - {self.status}"

    def save(self, *args, **kwargs):
        if not self.data_expiracao:
            self.data_expiracao = timezone.now() + timezone.timedelta(days=30)
        super().save(*args, **kwargs)

    def is_valid(self):
        if self.status == 'pendente' and timezone.now() <= self.data_expiracao:
            return True
        else:
            self.status = 'expirado'
            self.save()
            return False


class Recompensa(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tipo}"


class Sistema(models.Model):
    feedbacks = models.ManyToManyField(Feedback, related_name='sistemas')
    convites = models.ManyToManyField(Convite, related_name='sistemas')
    recompensas = models.ManyToManyField(Recompensa, related_name='sistemas')

    def registrar_feedback(self, membro, comentario):
        feedback = Feedback.objects.create(membro=membro, comentario=comentario)
        self.feedbacks.add(feedback)
        return feedback

    def visualizar_feedback(self):
        return self.feedbacks.all()

    def analisar_feedback(self):
        relatorio = Relatorio.objects.create()
        relatorio.feedbacks.set(self.feedbacks.all())
        return relatorio.gerar_relatorio()

    def registrar_convite(self, membro, convidado_email):
        # Limitar convites pendentes a 5
        if membro.convites_enviados.filter(status='pendente').count() >= 5:
            raise ValueError("Limite de convites pendentes atingido.")

        convite = Convite.objects.create(convidador=membro, convidado_email=convidado_email)
        self.convites.add(convite)
        return convite

    def validar_convite(self, convite, convidado_email):
        if not convite.is_valid():
            raise ValueError("Este convite expirou e não pode mais ser utilizado")

        convite.status = 'aceito'
        convite.convidado_email = convidado_email
        convite.save()
        return convite

    def conceder_recompensa(self, membro, recompensa):
        recompensa_instancia = Recompensa.objects.create(tipo=recompensa.tipo)
        membro.recompensas.add(recompensa_instancia)
        return recompensa_instancia


class Administrador(models.Model):
    user = models.OneToOneField(Membro, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user.username
