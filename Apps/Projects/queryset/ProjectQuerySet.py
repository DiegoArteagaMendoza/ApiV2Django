from Apps.Projects.models.ProjectsModels import Project

class ProjectQuerySet:
   
    # Get's
    @staticmethod
    def get_all_projects():
        return Project.objects.all()
    
    @staticmethod
    def get_projects_by_id(user_id):
        return Project.objects.filter(id=user_id).first()
    
    # Post's
    @staticmethod
    def create_projects(user_data):
        return Project.objects.create(**user_data)
    
    # Put's
    @staticmethod
    def update_project(user_id, updated_data):
        project = Project.objects.filter(id=user_id).first()
        if project:
            for key, value in updated_data.items():
                setattr(project, key, value)
            project.save()
        return project