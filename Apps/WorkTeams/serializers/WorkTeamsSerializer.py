from Apps.WorkTeams.models.WorkTeamModel import WorkTeam
from rest_framework import serializers

class WorkTeamSerializer(serializers.ModelSerializer):
    team_name = serializers.SerializerMethodField()
    team_project = serializers.SerializerMethodField()
    team_members = serializers.SerializerMethodField()

    class Meta:
        model = WorkTeam
        fields = '__all__'

    def get_team_name(self, obj):
        return f'{obj.team_name}'
    
    def get_team_project(self, obj):
        return f'{obj.team_project}'
    
    def get_team_members(self, obj):
        members = obj.team_members.all()
        return [f'Miembro: {member.user_name}' for member in members]
