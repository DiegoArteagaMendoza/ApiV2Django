from django import forms

class RegisterForm(forms.Form):
    ROLES = [
        ('Developer', 'Developer'),
        ('QA', 'QA'),
        ('GM', 'GM')
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
