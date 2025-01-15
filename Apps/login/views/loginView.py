from django.shortcuts import render
from django.http import JsonResponse
from Apps.login.forms.loginForm import LoginForm
from Apps.User.models.UserModel import User
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['GET', 'POST'])
def login(request):
    title = 'Login'
    if request.method == 'GET':
        return render(request, 'login.html', {
            'title': title,
            'form': LoginForm()
        })
    else:
        # Manejo de datos desde formulario HTML
        if request.content_type == 'application/x-www-form-urlencoded':
            userRut = request.POST.get('userRut')
            password = request.POST.get('password')
        else:  # Manejo de datos desde solicitud JSON
            userRut = request.data.get('userRut')
            password = request.data.get('password')
        
        try:
            user = User.objects.get(user_rut=userRut)

            if user.user_status == 0:
                return Response({"error": "Usuario no activo"}, status=400)
    
            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    "message": "Login exitoso",
                    "user": {
                        "user_name": user.user_name,
                        "user_last_name": user.user_last_name,
                        "user_email": user.user_email,
                        "user_role": user.user_role,
                        "tokens": {
                            "refresh": str(refresh),
                            "access": str(refresh.access_token),
                        }
                    }
                }, status=200)
            else:
                return Response({"error": "Credenciales incorrectas"}, status=400)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=404)
