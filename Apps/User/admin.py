from django.contrib import admin
from Apps.User.models.UserModel import User
from Apps.Projects.models.ProjectsModels import Project
from Apps.Tasks.models.TasksModels import Task
# Register your models here.

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Task)