from rest_framework import serializers
from .models import *


class CarreraSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField(required=False)
    codigo = serializers.CharField(required=False)

    class Meta:
        model = Carrera
        fields = ("id", "nombre", "codigo")


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = ("id", "nombre", "siglas")


class MateriaEnPlanSerializer(serializers.ModelSerializer):
    materia = serializers.SlugRelatedField(read_only=True, slug_field="nombre")
    plan = serializers.SlugRelatedField(read_only=True, slug_field="anio")
    area = serializers.SlugRelatedField(read_only=True, slug_field="nombre")
    obligatorias = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="codigo")
    recomendadas = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="codigo")

    class Meta:
        model = MateriaEnPlan
        fields = ("id", "materia", "plan", "nucleo",
                  "creditos", "area", "codigo", "obligatorias", "recomendadas", "cantidad_obligatoria_de")


class MateriaCursadaSerializer(serializers.ModelSerializer):
    materia = serializers.SlugRelatedField(read_only=True, slug_field="codigo")
    alumno = serializers.SlugRelatedField(read_only=True, slug_field="legajo")
    carrera = serializers.SlugRelatedField(read_only=True, slug_field="codigo")

    class Meta:
        model = MateriaCursada
        fields = ("materia", "nota", "alumno",
                  "carrera", "fecha", "resultado")


class InscripcionSerializer(serializers.ModelSerializer):
    materia = serializers.SlugRelatedField(read_only=True, slug_field="codigo")
    alumno = serializers.SlugRelatedField(read_only=True, slug_field="legajo")
    carrera = serializers.SlugRelatedField(read_only=True, slug_field="codigo")

    class Meta:
        model = Inscripcion
        fields = ("id", "materia", "alumno", "carrera", "fecha", "comision")


class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    cursadas = MateriaCursadaSerializer(many=True, required=False)

    class Meta:
        model = Alumno
        fields = ("id", "nombre", "apellido", "email", "legajo",
                  "es_regular", "cursadas", "es_regular")
