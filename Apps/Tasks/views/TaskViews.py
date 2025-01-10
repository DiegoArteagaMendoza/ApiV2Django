from Apps.Tasks.serializers.TaskSerializer import TaskSerializer
from Apps.Tasks.models.TasksModels import Task
from Apps.Tasks.queryset.TasksQuerySet import TaskQuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TaskListPostView(APIView):
    """
    Vista para manejar la lista de tareas (GET) y la creación de una nueva tarea (POST).
    """
    def get(self, request):
        tasks = TaskQuerySet.get_all_tasks()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskDetailView(APIView):
    """
    Vista para manejar la recuperación, actualización y elimincación de tareas
    """
    def get(self, request, task_id):
        task = TaskQuerySet.get_task_by_id(task_id)
        if task:
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"Error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, task_id):
        task = TaskQuerySet.get_task_by_id(task_id)
        if task:
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                updated_task = serializer.save()
                return Response(TaskSerializer(updated_task).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, task_id):
        task = TaskQuerySet.get_task_by_id(task_id)
        if task:
            task.delete()
            return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)