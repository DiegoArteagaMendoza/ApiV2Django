from Apps.WorkTeams.models.WorkTeamModel import WorkTeam

class WorkTeamQuerySet():
    # Get's
    @staticmethod
    def get_all_teams():
        return WorkTeam.objects.all()

    @staticmethod
    def get_team_by_id(work_team_id):
        return WorkTeam.objects.filter(id=work_team_id).first()
    
    # Post's
    @staticmethod
    def cerate_team_work(team_work_data):
        return WorkTeam.objects.create(**team_work_data)
    
    # Put's
    @staticmethod
    def update_team_work(team_work_id, updated_data):
        work_team = WorkTeam.objects.filter(id=team_work_id).first()
        if work_team:
            for key, value in updated_data.items():
                setattr(work_team, key, value)
            work_team.save()
        return work_team
    
    # Delete's
    @staticmethod
    def delete_team_work(work_team_id):
        work_team = WorkTeam.objects.filter(id=work_team_id).first()
        if work_team:
            work_team.delete()
        return work_team
    
    