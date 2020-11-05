from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        field = ['id', 'codigo_cuso', 'descricao', 'nivel']


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        field = ['id', 'aluno', 'cuso', 'periodo']