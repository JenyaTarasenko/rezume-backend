from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer


class ProjectListAPIViev(APIView):
    
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ProjectDetailView(APIView):
    def get(self, request, id):
        try:
            project = Project.objects.get(id=id)  # Получаем проект по ID
            serializer = ProjectSerializer(project)  # Сериализуем объект
            return Response(serializer.data)  # Возвращаем данные
        except Project.DoesNotExist:
            return Response({"error": "Проект не найден."}, status=status.HTTP_404_NOT_FOUND)
