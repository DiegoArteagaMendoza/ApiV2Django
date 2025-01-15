from django.shortcuts import render
from django.http import JsonResponse
from Apps.register.forms.registerForm import RegisterForm
from Apps.User.models.UserModel import User
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            'title': 'Register',
            'form': RegisterForm()
        })
    else:
        # Manejo de datos desde formulario HTML
        if request.content_type == 'application/x-www-form-urlencoded':
            userName = request.POST.get('userName')
            userLastName = request.POST.get('userLastName')
            userRut = request.POST.get('userRut')
            userEmail = request.POST.get('userEmail')
            userPhone = request.POST.get('userPhone')
            userRole = request.POST.get('userRole')
            userPassword = request.POST.get('userPassword')
            userConfirmPassword = request.POST.get('userConfirmPassword')
            isSuperuser = False  # No se maneja superusuario desde el formulario HTML
        else:  # Manejo de datos desde solicitud JSON
            userName = request.data.get('user_name')
            userLastName = request.data.get('user_last_name')
            userRut = request.data.get('user_rut')
            userEmail = request.data.get('user_email')
            userPhone = request.data.get('user_phone')
            userRole = request.data.get('user_role')
            userPassword = request.data.get('password')
            userConfirmPassword = request.data.get('userConfirmPassword')
            isSuperuser = request.data.get('is_superuser', False)  # Por defecto, False
        
        if userPassword != userConfirmPassword:
            return Response({"error": "Las contraseñas no coinciden"}, status=400)
            
        try:
            user = User.objects.create(
                user_name=userName,
                user_last_name=userLastName,
                user_email=userEmail,
                user_rut=userRut,
                user_phone=userPhone,
                password=make_password(userPassword),
                user_role=userRole,
                user_status=1,
                is_superuser=isSuperuser,
                is_staff=True if isSuperuser else False
            )
            
            # Generar tokens
            refresh = RefreshToken.for_user(user)
            tokens = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            
            return Response({
                "message": "Usuario creado exitosamente",
                "user": {
                    "user_name": user.user_name,
                    "user_last_name": user.user_last_name,
                    "user_email": user.user_email,
                    "user_role": user.user_role,
                    "tokens": tokens,
                }
            }, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
