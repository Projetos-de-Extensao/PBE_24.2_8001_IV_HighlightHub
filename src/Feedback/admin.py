from django.contrib import admin
from .models import Feedback, Relatorio, Membro

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('membro', 'avaliacao', 'data')
    list_filter = ('avaliacao', 'data')
    search_fields = ('usuario__username', 'texto')

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Relatorio)

try:
    admin.site.register(Membro)
except admin.sites.AlreadyRegistered:
    pass
