from django.db import models

# Create your models here.

class User(models.Model):
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
    user_email = models.EmailField(max_length=200)
    user_rut = models.CharField(max_length=10, null=False, default=00000000-0)
    user_phone = models.IntegerField(unique=True)
    user_password = models.CharField(max_length=50)
    user_role = models.CharField(max_length=100, choices=UserRole.choices, default=UserRole.NO_SELECTED)
    user_status = models.IntegerField(default=1) # 1 = active, 0 = not active
    
    def __str__(self):
        return f'{self.user_name} {self.user_last_name} - {self.user_role}'
    
    class Meta:
        db_table = 'user_table'