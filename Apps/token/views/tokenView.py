from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ObtenerToken(request):
    jwt_authenticator = JWTAuthentication()
    response = jwt_authenticator.authenticate(request)
    if response is not None:
        user, token = response
        return Response({"token": str(token)}, status=status.HTTP_200_OK)
    return Response({"error": "Token no encontrado"}, status=status.HTTP_400_BAD_REQUEST)