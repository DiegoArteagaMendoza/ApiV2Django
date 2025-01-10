from django.urls import path
from Apps.Projects.views.ProjectsView import ProjectsListPostView, ProjectDetailView

urlpatterns = [
    path('', ProjectsListPostView.as_view(), name='project_list'),  # Ruta para listar y crear proyectos
    path('<int:project_id>/', ProjectDetailView.as_view(), name='project_detail'),  # Ruta para detalles, actualización y eliminación
]
