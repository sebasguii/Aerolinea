from rest_framework.routers import DefaultRouter
from .views import AvionViewSet


router= DefaultRouter()

router.register(r'aviones', AvionViewSet, basename='avion')

urlpatterns = router.urls