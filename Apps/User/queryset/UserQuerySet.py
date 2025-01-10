from Apps.User.models.UserModel import User

class UserQuerySet:
    
    # Get's
    @staticmethod
    def get_all_users():
        return User.objects.all()
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.objects.filter(id=user_id).first()
    
    @staticmethod
    def get_all_active_users():
        return User.objects.filter(user_status=1)
    
    # Post's
    @staticmethod
    def create_user(user_data):
        return User.objects.create(**user_data)
    
    # Put's
    @staticmethod
    def update_user(user_id, updated_data):
        user = User.objects.filter(id=user_id).first()
        if user:
            for key, value in updated_data.items():
                setattr(user, key, value)
            user.save()
        return user
    
    @staticmethod
    def desactivate_user(user_id):
        user = User.objects.filter(id = user_id).first()
        if user:
            user.user_status = 0
            user.save()
        return user