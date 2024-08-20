from escola.models import Estudante, Curso, Matricula
from escola.serializers import (
    EstudanteSerializer,
    CursoSerializer,
    ListaMatriculasCursoSerializer,
    ListaMatriculasEstudanteSerializer,
    MatriculaSerializer,
)
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class EstudanteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudante(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset

    serializer_class  = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasCursoSerializer
