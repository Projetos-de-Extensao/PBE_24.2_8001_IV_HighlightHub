from django.contrib import admin
from .models import Feedback, Relatorio
from .models import Membro

admin.site.register(Feedback)
admin.site.register(Relatorio)
admin.site.register(Membro)
