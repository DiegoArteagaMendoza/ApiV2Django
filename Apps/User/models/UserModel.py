from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=200, unique=True)
    user_phone = models.IntegerField(unique=True)
    user_password = models.CharField(max_length=50)
    user_role = models.CharField(max_length=100)
    user_status = models.IntegerField(default=1) # 1 = active, 0 = not active
    
    def __str__(self):
        return f'{self.user_name} {self.user_last_name} - {self.user_role}'
    
    class Meta:
        db_table = 'user_table'