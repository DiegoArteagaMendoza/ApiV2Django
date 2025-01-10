from django.db import models
from Apps.User.models.UserModel import User
from Apps.Projects.models.ProjectsModels import Project 

# Create your models here.
        
class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    task_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tasks')
    task_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_tasks')
    
    def __str__(self):
        return f'Task: {self.task_name} - User assigned: {self.task_user} - Project assigned: {self.task_project}'
    
    class Meta:
        db_table = 'tasks_table'