from Apps.Projects.serializers.ProjectSerializer import ProjectSerializer
from Apps.Projects.queryset.ProjectQuerySet import ProjectQuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProjectsListPostView(APIView):
    """
    Vista para manejar la lista de proyectos (GET) y la creación de un nuevo proyecto (POST).
    """
    def get(self, request):
        projects = ProjectQuerySet.get_all_projects()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailView(APIView):
    """
    Vista para manejar la recuperación, actualización y eliminación de un proyecto específico.
    """
    def get(self, request, project_id):
        project = ProjectQuerySet.get_projects_by_id(project_id)
        if project:
            serializer = ProjectSerializer(project)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, project_id):
        project = ProjectQuerySet.get_projects_by_id(project_id)
        if project:
            serializer = ProjectSerializer(project, data=request.data, partial=True)
            if serializer.is_valid():
                updated_project = serializer.save()
                return Response(ProjectSerializer(updated_project).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, project_id):
        project = ProjectQuerySet.get_projects_by_id(project_id)
        if project:
            project.delete()
            return Response({"message": "Project deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
