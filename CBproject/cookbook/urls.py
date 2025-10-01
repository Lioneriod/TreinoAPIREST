from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngredienteViewSet, ReceitaViewSet

router = DefaultRouter()
router.register(r'ingredientes', IngredienteViewSet)
router.register(r'receitas', ReceitaViewSet)

urlpatterns = [
    path('api/', include(router.urls))
    ]
