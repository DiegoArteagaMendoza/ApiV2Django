from django.urls import path
from Apps.Tasks.views.TaskViews import TaskListPostView, TaskDetailView

urlpatterns = [
    path('', TaskListPostView.as_view(), name='task_list'),
    path('<int:task_id>/', TaskDetailView.as_view(), name='task_detail')
]