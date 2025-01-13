from Apps.Tasks.models.TasksModels import Task
from Apps.WorkTeams.models.WorkTeamModel import WorkTeam
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()
    
    class Meta:        
        model = Task
        fields = ['id', 'task_name', 'task_description', 'user_name', 'project_name', 'task_status', 'team_name']        
        
    def get_team_name(self, obj):
        return obj.task_team.team_name if obj.task_team else None
    
    def get_user_name(self, obj):
        return obj.task_user.user_name if obj.task_user else None
    
    def get_project_name(self, obj):
        return obj.task_project.project_name if obj.task_project else None
   
    
    def create(self, validate_data):
        return Task.objects.create(**validate_data)