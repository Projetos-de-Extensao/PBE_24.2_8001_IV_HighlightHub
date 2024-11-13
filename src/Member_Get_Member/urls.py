from rest_framework.routers import DefaultRouter
from .views import ConviteViewSet, RecompensaViewSet, SistemaViewSet

router = DefaultRouter()
router.register(r'convites', ConviteViewSet)  
router.register(r'recompensas', RecompensaViewSet)  
router.register(r'sistemas', SistemaViewSet)  

urlpatterns = router.urls
