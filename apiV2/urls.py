from django.contrib import admin
from django.urls import path, include
# urls
from Apps.User.urls import urls as UserUrls
from Apps.Projects.urls import urls as ProjectsUrls
from Apps.Tasks.urls import urls as TasksUrls
from Apps.WorkTeams.urls import urls as WorkTeamUrls
from Apps.login.urls import urls as LoginUrls
from Apps.register.urls import urls as RegisterUrls
from Apps.pdfMaker.urls import urls as PdfUrls
from Apps.ExcelMaker.urls import urls as ExcelUrls
from Apps.logout.urls import urls as LogoutUrls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(UserUrls), name='user_urls'),
    path('project/', include(ProjectsUrls), name='project_urls'),
    path('tasks/', include(TasksUrls), name='tasks_urls'),
    path('workteam/', include(WorkTeamUrls), name='work_team_urls'),
    path('login/', include(LoginUrls)),
    path('register/', include(RegisterUrls)),
    path('descarga-pdf/', include(PdfUrls)),
    path('descargar-xlsx/', include(ExcelUrls)),
    path('logout/', include(LogoutUrls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)