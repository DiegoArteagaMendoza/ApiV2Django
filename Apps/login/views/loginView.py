# from django.shortcuts import render
# from django.http import JsonResponse
# from Apps.login.forms.loginForm import LoginForm
# from Apps.User.models.UserModel import User
# from django.contrib.auth.hashers import check_password
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken

# @api_view(['GET', 'POST'])
# def login(request):
#     title = 'Login'
#     if request.method == 'GET':
#         return render(request, 'login.html', {
#             'title': title,
#             'form': LoginForm()
#         })
#     else:
#         # Manejo de datos desde formulario HTML
#         if request.content_type == 'application/x-www-form-urlencoded':
#             userRut = request.POST.get('userRut')
#             password = request.POST.get('password')
#         else:  # Manejo de datos desde solicitud JSON
#             userRut = request.data.get('userRut')
#             password = request.data.get('password')
        
#         try:
#             user = User.objects.get(user_rut=userRut)

#             if user.user_status == 0:
#                 return JsonResponse({"error": "Usuario no activo"}, status=400)
    
#             if check_password(password, user.password):
#                 refresh = RefreshToken.for_user(user)
#                 response_data = {
#                     "message": "Login exitoso",
#                     "user": {
#                         "user_name": user.user_name,
#                         "user_last_name": user.user_last_name,
#                         "user_email": user.user_email,
#                         "user_role": user.user_role,
#                         "tokens": {
#                             "refresh": str(refresh),
#                             "access": str(refresh.access_token),
#                         }
#                     }
#                 }
#                 if request.content_type == 'application/x-www-form-urlencoded':
#                     return render(request, 'login_success.html', response_data)
#                 return JsonResponse(response_data, status=200)
#             else:
#                 return JsonResponse({"error": "Credenciales incorrectas"}, status=400)
#         except User.DoesNotExist:
#             return JsonResponse({"error": "Usuario no encontrado"}, status=404)

from django.shortcuts import render
from django.http import JsonResponse
from Apps.login.forms.loginForm import LoginForm
from Apps.User.models.UserModel import User
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
import logging

logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def login(request):
    title = 'Login'
    if request.method == 'GET':
        return render(request, 'login.html', {
            'title': title,
            'form': LoginForm()
        })
    else:
        userRut = request.data.get('userRut')
        password = request.data.get('password')
        
        try:
            user = User.objects.get(user_rut=userRut)

            if user.user_status == 0:
                logger.info("Usuario no activo")
                return JsonResponse({"error": "Usuario no activo"}, status=400)
    
            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                response_data = {
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
                }
                logger.info("Login exitoso para el usuario: %s", user.user_rut)
                return JsonResponse(response_data, status=200)
            else:
                logger.info("Credenciales incorrectas para el usuario: %s", userRut)
                return JsonResponse({"error": "Credenciales incorrectas"}, status=400)
        except User.DoesNotExist:
            logger.info("Usuario no encontrado: %s", userRut)
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
        except Exception as e:
            logger.error("Error en el servidor: %s", str(e))
            return JsonResponse({"error": "Error en el servidor"}, status=500)
