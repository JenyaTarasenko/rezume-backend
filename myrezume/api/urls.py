from django.contrib import admin
from django.urls import path, include
from .views import ProjectListAPIViev, ProjectDetailView



app_name = 'api'

urlpatterns = [
    
    path('projects/', ProjectListAPIViev.as_view(), name='project-list'),#Первая страничка 
    path('projects/<int:id>/', ProjectDetailView.as_view(), name='project-detail'), # Детали проекта

    
]    
