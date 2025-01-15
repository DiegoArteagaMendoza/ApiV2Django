from django import forms

class RegisterForm(forms.Form):
    ROLES = [
        ('DEV', 'Desarrollador'),
        ('QA', 'Quality Assurance'),
        ('PM', 'Project Manager'),
        ('UX', 'Diseñador de Experiencia de Usuario'),
        ('UI', 'Diseñador de Interfaz de Usuario'),
        ('PO', 'Product Owner'),
        ('BA', 'Business Analyst'),
        ('CTO', 'Chief Technology Officer'),
        ('CEO', 'Chief Executive Officer'),
        ('COO', 'Chief Operating Officer'),
        ('HR', 'Recursos Humanos'),
        ('SM', 'Scrum Master'),
        ('DEVOPS', 'Ingeniero DevOps'),
        ('SYS_ADMIN', 'Administrador de Sistemas'),
        ('DBA', 'Administrador de Base de Datos'),
        ('FRONTEND', 'Desarrollador Frontend'),
        ('BACKEND', 'Desarrollador Backend'),
        ('FULLSTACK', 'Desarrollador Fullstack'),
        ('DS', 'Científico de Datos'),
        ('DE', 'Ingeniero de Datos'),
        ('ML', 'Ingeniero de Machine Learning'),
        ('SUPPORT', 'Soporte Técnico'),
        ('SECURITY', 'Especialista en Seguridad'),
        ('MARKETING', 'Marketing'),
        ('SALES', 'Ventas'),
        ('CS', 'Éxito del Cliente'),
        ('NS', 'No seleccionado')
    ]

    
    userName = forms.CharField(label='Nombre de usuario', max_length=50, required=True)
    userLastName = forms.CharField(label='Apellido', max_length=50, required=True)
    userRut = forms.CharField(label='Rut', max_length=10, required=True)
    userEmail = forms.EmailField(label='Correo electrónico', max_length=200, required=True)
    userPhone = forms.CharField(label='Teléfono', max_length=10, required=True)
    userRole = forms.ChoiceField(choices=ROLES, label='Rol', required=True)
    userPassword = forms.CharField(
        label='Contraseña',
        max_length=50,
        required=True,
        widget=forms.PasswordInput
    )
    userConfirmPassword = forms.CharField(
        label='Confirmar contraseña',
        max_length=50,
        required=True,
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('userPassword')
        confirm_password = cleaned_data.get('userConfirmPassword')

        if password and confirm_password and password != confirm_password:
            self.add_error('userConfirmPassword', 'Las contraseñas no coinciden.')
