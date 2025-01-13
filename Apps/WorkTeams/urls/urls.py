from django.urls import path
from Apps.WorkTeams.views.WorkTeamsView import WorkTeamDetailView, WorkTeamListPostView

urlpatterns = [
    path('', WorkTeamListPostView.as_view(), name='work_team_list'),
    path('<int:work_team_id>/', WorkTeamDetailView.as_view(), name='work_team_detail')
]