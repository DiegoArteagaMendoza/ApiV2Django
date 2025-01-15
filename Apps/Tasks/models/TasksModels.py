from django.db import models
from Apps.User.models.UserModel import User
from Apps.Projects.models.ProjectsModels import Project
from Apps.WorkTeams.models.WorkTeamModel import WorkTeam

# Create your models here.
        
class Task(models.Model):
    class TaskStatus(models.TextChoices):
        NEW = 'NEW', 'Nuevo'
        IN_PROGRES = 'IN_PROGRES', 'En Progreso'
        COMPLETED = 'COMPLETED', 'Completado'
        
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    task_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tasks')
    task_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_tasks')
    task_status = models.CharField(max_length=20, choices=TaskStatus.choices, default=TaskStatus.NEW)
    task_team = models.ForeignKey(WorkTeam, on_delete=models.CASCADE, related_name='team_tasks', null=True, blank=True)
    task_date_create = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.task_name} - {self.task_user} - {self.task_project} - {self.task_team}'
    
    class Meta:
        db_table = 'tasks_table'