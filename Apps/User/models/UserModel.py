from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, user_email, user_password=None, **extra_fields):
        if not user_email:
            raise ValueError("El usuario debe tener un correo electrónico")
        user_email = self.normalize_email(user_email)
        user = self.model(user_email=user_email, **extra_fields)
        user.set_password(user_password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, user_email, user_password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(user_email, user_password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    class UserRole(models.TextChoices):
        DEV = 'DEV', 'Desarrollador'
        QA = 'QA', 'Quality Assurance'
        PM = 'PM', 'Project Manager'
        UX = 'UX', 'Diseñador de Experiencia de Usuario'
        UI = 'UI', 'Diseñador de Interfaz de Usuario'
        PO = 'PO', 'Product Owner'
        BA = 'BA', 'Business Analyst'
        CTO = 'CTO', 'Chief Technology Officer'
        CEO = 'CEO', 'Chief Executive Officer'
        COO = 'COO', 'Chief Operating Officer'
        HR = 'HR', 'Recursos Humanos'
        SCRUM_MASTER = 'SM', 'Scrum Master'
        DEVOPS = 'DEVOPS', 'Ingeniero DevOps'
        SYS_ADMIN = 'SYS_ADMIN', 'Administrador de Sistemas'
        DATABASE_ADMIN = 'DBA', 'Administrador de Base de Datos'
        FRONTEND = 'FRONTEND', 'Desarrollador Frontend'
        BACKEND = 'BACKEND', 'Desarrollador Backend'
        FULLSTACK = 'FULLSTACK', 'Desarrollador Fullstack'
        DATA_SCIENTIST = 'DS', 'Científico de Datos'
        DATA_ENGINEER = 'DE', 'Ingeniero de Datos'
        ML_ENGINEER = 'ML', 'Ingeniero de Machine Learning'
        SUPPORT = 'SUPPORT', 'Soporte Técnico'
        SECURITY = 'SECURITY', 'Especialista en Seguridad'
        MARKETING = 'MARKETING', 'Marketing'
        SALES = 'SALES', 'Ventas'
        CUSTOMER_SUCCESS = 'CS', 'Éxito del Cliente'
        NO_SELECTED = 'NS', 'No seleccionado'
    
    user_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    user_email = models.EmailField(unique=True, max_length=200)
    user_rut = models.CharField(max_length=10, null=False, default='00000000-0')
    user_phone = models.IntegerField(unique=True)
    user_role = models.CharField(max_length=100, choices=UserRole.choices, default=UserRole.NO_SELECTED)
    user_status = models.IntegerField(default=1) # 1 = active, 0 = not active
    password = models.CharField(max_length=128, default=make_password("defaultpassword123"))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_name', 'user_last_name', 'user_phone']
    
    def __str__(self):
        return f'{self.user_name} {self.user_last_name} - {self.user_role}'
    
    class Meta:
        db_table = 'user_table'
