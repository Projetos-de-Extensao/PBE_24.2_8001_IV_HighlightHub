from rest_framework.routers import DefaultRouter
from .views import ConviteViewSet, RecompensaViewSet, SistemaViewSet

router = DefaultRouter()
router.register(r'convites', ConviteViewSet)  # Endpoint para convites
router.register(r'recompensas', RecompensaViewSet)  # Endpoint para recompensas
router.register(r'sistemas', SistemaViewSet)  # Endpoint para sistemas

urlpatterns = router.urls
