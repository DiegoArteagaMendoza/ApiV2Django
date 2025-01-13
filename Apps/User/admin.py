from django.contrib import admin
from Apps.User.models.UserModel import User
from Apps.Projects.models.ProjectsModels import Project
from Apps.Tasks.models.TasksModels import Task
from Apps.WorkTeams.models.WorkTeamModel import WorkTeam
# Register your models here.

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(WorkTeam)