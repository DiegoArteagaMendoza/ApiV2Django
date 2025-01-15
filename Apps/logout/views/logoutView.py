from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

@api_view(['POST'])
def logout(request):
    try:
        # Obtener el token de refresco del cuerpo de la solicitud
        refresh_token = request.data['refresh']
        token = RefreshToken(refresh_token)
        token.blacklist()
        
        return Response({"message": "Cierre de sesión exitoso"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
