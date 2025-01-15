from django.urls import path
from Apps.WorkTeams.views import WorkTeamsView
urlpatterns = [
    # Ruta para obtener la lista de equipos de trabajo
    path('list/', WorkTeamsView.ObtenerEquipos, name='work_team_list'),

    # Ruta para crear un nuevo equipo de trabajo
    path('create/', WorkTeamsView.CrearEquipo, name='work_team_create'),

    # Ruta para obtener los detalles de un equipo específico
    path('details/<int:work_team_id>/', WorkTeamsView.VerEquipo, name='work_team_detail'),

    # Ruta para actualizar un equipo específico
    path('update/<int:work_team_id>/', WorkTeamsView.ActualizarEquipo, name='work_team_update'),

    # Ruta para eliminar un equipo específico
    path('delete/<int:work_team_id>/', WorkTeamsView.EliminarEquipo, name='work_team_delete'),
]
