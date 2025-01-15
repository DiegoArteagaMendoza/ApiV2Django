from Apps.User.serializers.UserSerializer import UserSerializer
from Apps.User.queryset.UserQuerySet import UserQuerySet
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

@api_view(['GET'])
def ObtenerUsuarios(request):
    users = UserQuerySet.get_all_users()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def CrearUsuario(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.validate_duplicate_user(serializer.validated_data)
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET'])
def VerUsuario(request, user_id):
    user = UserQuerySet.get_user_by_id(user_id)
    if not user:
        return Response(
            {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
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
