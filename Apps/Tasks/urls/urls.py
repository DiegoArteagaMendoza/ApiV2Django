# from django.urls import path
# from Apps.Tasks.views.TaskViews import TaskListPostView, TaskDetailView

# urlpatterns = [
#     path('', TaskListPostView.as_view(), name='task_list'),
#     path('<int:task_id>/', TaskDetailView.as_view(), name='task_detail')
# ]

from django.urls import path
from Apps.Tasks.views import TaskViews

urlpatterns = [
    # Ruta para obtener la lista de tareas
    path('list/', TaskViews.ObtenerTareas, name='task_list'),

    # Ruta para crear una nueva tarea
    path('create/', TaskViews.CrearTarea, name='task_create'),

    # Ruta para obtener el detalle de una tarea específica
    path('details/<int:task_id>/', TaskViews.VerTarea, name='task_detail'),

    # Ruta para actualizar una tarea específica
    path('update/<int:task_id>/', TaskViews.ActualizarTarea, name='task_update'),

    # Ruta para eliminar una tarea específica
    path('delete/<int:task_id>/', TaskViews.EliminarTarea, name='task_delete'),
]
