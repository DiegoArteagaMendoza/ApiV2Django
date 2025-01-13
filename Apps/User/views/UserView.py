from Apps.User.serializers.UserSerializer import UserSerializer
from Apps.User.queryset.UserQuerySet import UserQuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserListPostView(APIView):
    def get(self, request):
        users = UserQuerySet.get_all_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.validate_duplicate_user(serializer.validated_data)
                user = serializer.save()
                return Response(
                    UserSerializer(user).data, status=status.HTTP_201_CREATED
                )
            except serializer.ValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetailView(APIView):
    def get(self, request, user_id):
        user = UserQuerySet.get_user_by_id(user_id)
        if not user:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
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

    def delete(self, request, user_id):
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