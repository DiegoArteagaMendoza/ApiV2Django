from Apps.WorkTeams.serializers.WorkTeamsSerializer import WorkTeamSerializer
from Apps.WorkTeams.models.WorkTeamModel import WorkTeam
from Apps.WorkTeams.queryset.WorkTeamQuerySet import WorkTeamQuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class WorkTeamListPostView(APIView):
    """
    Vista para manejar la lista de equipos (GET) y la creación de equipos (POST)
    """
    
    def get(self, request):
        work_team = WorkTeamQuerySet.get_all_teams()
        serializer = WorkTeamSerializer(work_team, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = WorkTeamSerializer(data=request.data)
        if serializer.is_valid():
            work_team = serializer.save()
            return Response(WorkTeamSerializer(work_team).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WorkTeamDetailView(APIView):
    """
    Vista para manejar la recuperación, actualización y eliminación de equipos
    """
    
    def get(self, request, work_team_id):
        work_team = WorkTeamQuerySet.get_team_by_id(work_team_id)
        if work_team:
            serializer = WorkTeamSerializer(work_team)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"Error":"Work team not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, work_team_id):
        work_team = WorkTeamQuerySet.get_team_by_id(work_team_id)
        if work_team:
            serializer = WorkTeamSerializer(work_team, data=request.data, partial=True)
            if serializer.is_valid():
                updated_team_work = serializer.save()
                return Response(WorkTeamSerializer(updated_team_work).data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return "Team not found"
    
    def delete(self, request, work_team_id):
        work_team = WorkTeamQuerySet.get_team_by_id(work_team_id)
        if work_team:
            work_team.delete()
            return Response({"message":"Work team deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({"error": "Work team not found"}, status=status.HTTP_404_NOT_FOUND)
        
    