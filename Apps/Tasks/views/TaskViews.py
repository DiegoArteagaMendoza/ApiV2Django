from Apps.Tasks.serializers.TaskSerializer import TaskSerializer
from Apps.Tasks.models.TasksModels import Task
from Apps.Tasks.queryset.TasksQuerySet import TaskQuerySet
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def ObtenerTareas(request):
    tasks = TaskQuerySet.get_all_tasks()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def CrearTarea(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        task = serializer.save()
        return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def VerTarea(request, task_id):
    task = TaskQuerySet.get_task_by_id(task_id)
    if task:
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"Error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def ActualizarTarea(request, task_id):
    task = TaskQuerySet.get_task_by_id(task_id)
    if task:
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            updated_task = serializer.save()
            return Response(TaskSerializer(updated_task).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def EliminarTarea(request, task_id):
    task = TaskQuerySet.get_task_by_id(task_id)
    if task:
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)