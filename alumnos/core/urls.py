from django.urls import path, include
from .views import *
from rest_framework import routers, serializers, viewsets, generics

router = routers.DefaultRouter()
router.register(r'materias', MateriasView)
router.register(r'alumnos', AlumnosView)
router.register(r'personas', PersonasView)
router.register(r'comisiones', ComisionView)
router.register(r'carreras', CarrerasView)
router.register(r'inscripciones', InscripcionesView)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
