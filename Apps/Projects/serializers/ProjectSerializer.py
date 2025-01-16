from Apps.Projects.models.ProjectsModels import Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    project_image = serializers.ImageField(required=False)
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'project_description', 'project_budget', 'project_start_date', 'project_image']
        
    def create(self, validate_data):
        return Project.objects.create(**validate_data)