# from django.urls import path
# from Apps.WorkTeams.views.WorkTeamsView import WorkTeamDetailView, WorkTeamListPostView

# urlpatterns = [
#     path('', WorkTeamListPostView.as_view(), name='work_team_list'),
#     path('<int:work_team_id>/', WorkTeamDetailView.as_view(), name='work_team_detail')
# ]

from django.urls import path
from Apps.WorkTeams.views.WorkTeamsView import WorkTeamListPostView, WorkTeamDetailView

urlpatterns = [
    # Ruta para obtener la lista de equipos de trabajo
    path('list/', WorkTeamListPostView.as_view(), name='work_team_list'),

    # Ruta para crear un nuevo equipo de trabajo
    path('create/', WorkTeamListPostView.as_view(), name='work_team_create'),

    # Ruta para obtener los detalles de un equipo específico
    path('details/<int:work_team_id>/', WorkTeamDetailView.as_view(), name='work_team_detail'),

    # Ruta para actualizar un equipo específico
    path('update/<int:work_team_id>/', WorkTeamDetailView.as_view(), name='work_team_update'),

    # Ruta para eliminar un equipo específico
    path('delete/<int:work_team_id>/', WorkTeamDetailView.as_view(), name='work_team_delete'),
]
