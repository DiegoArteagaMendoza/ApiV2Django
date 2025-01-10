from ..models import ProjectsModels as Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'project_description', 'project_budget', 'project_start_date']
        
    def create(self, validate_data):
        return Project.objects.create(**validate_data)