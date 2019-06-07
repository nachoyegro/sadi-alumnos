from .models import *
from .serializers import *
from rest_framework import viewsets, renderers, generics
from rest_framework.response import Response

class InscripcionesView(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

class PersonasView(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class AlumnosView(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class MateriasView(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class ComisionView(viewsets.ModelViewSet):
    queryset = Comision.objects.all()
    serializer_class = ComisionSerializer

class CarrerasView(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer