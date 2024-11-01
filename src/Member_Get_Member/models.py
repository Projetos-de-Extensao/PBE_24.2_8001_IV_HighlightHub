from django.db import models
from Feedback.models import Membro, Feedback  # Import apenas de Membro e Feedback necessários
from Feedback.models import Relatorio

class Convite(models.Model):
    convidador = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='convites_enviados')
    convidado = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='convites_recebidos')
    status = models.CharField(max_length=20, default='pendente')

    def __str__(self):
        return f"Convite de {self.convidador.user.username} para {self.convidado.user.username} - {self.status}"

class Recompensa(models.Model):
    tipo = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tipo} - {self.valor}"

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
        # Cria um objeto de Relatorio
        relatorio = Relatorio.objects.create()
        # Adiciona os feedbacks ao relatorio
        relatorio.feedbacks.set(self.feedbacks.all())
        # Gera o relatório
        return relatorio.gerar_relatorio()

    def registrar_convite(self, membro, convite):
        convite_instancia = Convite.objects.create(convidador=membro, convidado=convite)
        self.convites.add(convite_instancia)
        return convite_instancia

    def validar_convite(self, convite):
        convite.status = "aceito"
        convite.save()
        return convite

    def conceder_recompensa(self, membro, recompensa):
        recompensa_instancia = Recompensa.objects.create(tipo=recompensa.tipo, valor=recompensa.valor)
        membro.recompensas.add(recompensa_instancia)
        return recompensa_instancia

class Administrador(models.Model):
    user = models.OneToOneField(Membro, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user.username
