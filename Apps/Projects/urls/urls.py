from django.urls import path
from Apps.Projects.views import ProjectsView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Ruta para obtener la lista de proyectos
    path('list/', ProjectsView.ObtenerProyectos, name='project_list'),

    # Ruta para crear un nuevo proyecto
    path('create/', ProjectsView.CrearProyecto, name='project_create'),

    # Ruta para obtener los detalles de un proyecto específico
    path('details/<int:project_id>/', ProjectsView.VerProyecto, name='project_detail'),

    # Ruta para actualizar un proyecto específico
    path('update/<int:project_id>/', ProjectsView.ActualizarProyecto, name='project_update'),

    # Ruta para eliminar un proyecto específico
    path('delete/<int:project_id>/', ProjectsView.EliminarProyecto, name='project_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
