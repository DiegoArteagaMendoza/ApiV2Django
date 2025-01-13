# from django.urls import path
# from Apps.Projects.views.ProjectsView import ProjectsListPostView, ProjectDetailView

# urlpatterns = [
#     path('', ProjectsListPostView.as_view(), name='project_list'),  # Ruta para listar y crear proyectos
#     path('<int:project_id>/', ProjectDetailView.as_view(), name='project_detail'),  # Ruta para detalles, actualización y eliminación
# ]


from django.urls import path
from Apps.Projects.views.ProjectsView import ProjectsListPostView, ProjectDetailView

urlpatterns = [
    # Ruta para obtener la lista de proyectos
    path('list/', ProjectsListPostView.as_view(), name='project_list'),

    # Ruta para crear un nuevo proyecto
    path('create/', ProjectsListPostView.as_view(), name='project_create'),

    # Ruta para obtener los detalles de un proyecto específico
    path('details/<int:project_id>/', ProjectDetailView.as_view(), name='project_detail'),

    # Ruta para actualizar un proyecto específico
    path('update/<int:project_id>/', ProjectDetailView.as_view(), name='project_update'),

    # Ruta para eliminar un proyecto específico
    path('delete/<int:project_id>/', ProjectDetailView.as_view(), name='project_delete'),
]
