from django.db import models

# Create your models here.
    
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_budget = models.IntegerField()
    project_start_date = models.DateField()
    project_image = models.ImageField(upload_to="projectImages", null=True, blank=True)
    
    def __str__(self):
        return f'{self.project_name}'
    
    class Meta:
        db_table = 'projects_table'