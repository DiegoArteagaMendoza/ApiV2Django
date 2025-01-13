from Apps.Tasks.models.TasksModels import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'task_description', 'task_user', 'task_project', 'task_status']        
        
    def create(self, validate_data):
        return Task.objects.create(**validate_data)