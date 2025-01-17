from Apps.User.serializers.UserSerializer import UserSerializer
from Apps.User.queryset.UserQuerySet import UserQuerySet
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ObtenerUsuarios(request):
    users = UserQuerySet.get_all_users()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def CrearUsuario(request):
    data = request.data.copy()
    
    # Verificar si hay un archivo 'user_image' en los datos
    if 'user_image' in request.FILES:
        data['user_image'] = request.FILES['user_image']
    # Serializar los datos
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        try:
            # Validar duplicados (esto parece ser una función personalizada en tu serializador)
            serializer.validate_duplicate_user(serializer.validated_data)
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    # Devolver errores si el serializador no es válido
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def VerUsuario(request, user_id):
    user = UserQuerySet.get_user_by_id(user_id)
    if not user:
        return Response(
            {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def ActualizarUsuario(request, user_id):
    user = UserQuerySet.get_user_by_id(user_id)
    if not user:
        return Response(
            {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        user = UserQuerySet.update_user(user_id, serializer.validated_data)
        return Response(
            UserSerializer(user).data, status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def EliminarUsuario(request, user_id):
    user = UserQuerySet.get_user_by_id(user_id)
    if not user:
        return Response(
            {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
        )

    user = UserQuerySet.desactivate_user(user_id)
    return Response(
        {"message": "User deactivated successfully"},
        status=status.HTTP_200_OK,
    )
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def PerfilUsuario(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
