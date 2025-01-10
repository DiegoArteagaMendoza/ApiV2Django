from Apps.Tasks.models.TasksModels import Task

class TaskQuerySet:
    # Get's
    @staticmethod
    def get_all_tasks():
        return Task.objects.all()

    @staticmethod
    def get_task_by_id(task_id):
        return Task.objects.filter(id=task_id).first()

    @staticmethod
    def get_tasks_by_user(user_id):
        return Task.objects.filter(task_user__id=user_id)

    @staticmethod
    def get_tasks_by_project(project_id):
        return Task.objects.filter(task_project__id=project_id)

    @staticmethod
    def get_tasks_by_user_and_project(user_id, project_id):
        return Task.objects.filter(task_user__id=user_id, task_project__id=project_id)

    # Post's
    @staticmethod
    def create_task(task_data):
        return Task.objects.create(**task_data)

    # Put's
    @staticmethod
    def update_task(task_id, updated_data):
        task = Task.objects.filter(id=task_id).first()
        if task:
            for key, value in updated_data.items():
                setattr(task, key, value)
            task.save()
        return task

    # Delete's
    @staticmethod
    def delete_task(task_id):
        task = Task.objects.filter(id=task_id).first()
        if task:
            task.delete()
        return task
