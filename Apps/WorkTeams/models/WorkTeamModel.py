from django.db import models
from Apps.User.models.UserModel import User
from Apps.Projects.models.ProjectsModels import Project 

class WorkTeam(models.Model):
    team_name = models.CharField(max_length=50)
    team_date_create = models.DateField(auto_now_add=False)
    team_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='team_project')
    team_members = models.ManyToManyField(User, related_name='team_members')
    
    def __str__(self):
        return self.team_name
    
    class Meta:
        db_table = 'team_table'