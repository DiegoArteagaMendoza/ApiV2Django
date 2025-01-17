from Apps.WorkTeams.serializers.WorkTeamsSerializer import WorkTeamSerializer
from Apps.WorkTeams.models.WorkTeamModel import WorkTeam
from Apps.WorkTeams.queryset.WorkTeamQuerySet import WorkTeamQuerySet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ObtenerEquipos(request):
    work_team = WorkTeamQuerySet.get_all_teams()
    serializer = WorkTeamSerializer(work_team, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CrearEquipo(request):
    serializer = WorkTeamSerializer(data=request.data)
    if serializer.is_valid():
        work_team = serializer.save()
        return Response(WorkTeamSerializer(work_team).data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def VerEquipo(request, work_team_id):
    work_team = WorkTeamQuerySet.get_team_by_id(work_team_id)
    if work_team:
        serializer = WorkTeamSerializer(work_team)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response({"Error":"Work team not found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def ActualizarEquipo(request, work_team_id):
    work_team = WorkTeamQuerySet.get_team_by_id(work_team_id)
    if work_team:
        serializer = WorkTeamSerializer(work_team, data=request.data, partial=True)
        if serializer.is_valid():
            updated_team_work = serializer.save()
            return Response(WorkTeamSerializer(updated_team_work).data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return "Team not found"

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def EliminarEquipo(request, work_team_id):
    work_team = WorkTeamQuerySet.get_team_by_id(work_team_id)
    if work_team:
        work_team.delete()
        return Response({"message":"Work team deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    return Response({"error": "Work team not found"}, status=status.HTTP_404_NOT_FOUND)
    
