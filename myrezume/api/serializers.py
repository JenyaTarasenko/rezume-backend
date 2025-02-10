from rest_framework import serializers
from .models import Project
from django.conf import settings


class ProjectSerializer(serializers.ModelSerializer):
    
    # image = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = ['id', 'name', 'slug', 'description', 'image', 'link', 'tehnology_project']
        
    # def get_image_logo_url(self, obj):
    #     return f"{settings.MEDIA_URL}{obj.image_logo}" if obj.image_logo else None
        # return obj.image_logo.url if obj.image_logo else None
    
    # def get_image(self, obj):
    #     request = self.context.get('request')
    #     return request.build_absolute_uri(obj.image.url)
    
   
    # def get_image_url(self, obj):
    #     return f"{settings.MEDIA_URL}{obj.image}" if obj.image else None
        # return obj.image.url if obj.image else None
        