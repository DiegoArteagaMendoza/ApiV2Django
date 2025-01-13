from django.db import models
from Apps.User.models.UserModel import User
from Apps.Projects.models.ProjectsModels import Project 

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
    
    def __str__(self):
        return f'{self.task_name} - {self.task_user} - {self.task_project}'
    
    class Meta:
        db_table = 'tasks_table'