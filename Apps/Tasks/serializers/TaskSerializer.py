from ..models import TasksModels as Tasks
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'task_name', 'task_description', 'task_user', 'task_project']
        
    def create(self, validate_data):
        return Tasks.objects.create(**validate_data)