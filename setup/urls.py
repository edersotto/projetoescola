from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAlunoViewSet, ListaAlunosMatriculadosCursoViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet)
router.register('cursos', CursosViewSet)
router.register('matriculas', MatriculasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAlunoViewSet.as_view()),
    path('curso/<int:pk>/matriculas/',  ListaAlunosMatriculadosCursoViewSet.as_view())
]
