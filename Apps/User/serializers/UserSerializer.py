from Apps.User.models.UserModel import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

# class UserSerializer(serializers.ModelSerializer):
#     user_role = serializers.SerializerMethodField()
#     user_status = serializers.SerializerMethodField()
#     tokens = serializers.SerializerMethodField()
#     user_image = serializers.ImageField(required=False)
    
#     class Meta:
#         model = User
#         fields = '__all__'
    
#     def get_user_role(self, obj):
#         return f'{obj.user_role}'
    
#     def get_user_status(self, obj):
#         return "active" if obj.user_status == 1 else "not active"
    
#     def get_tokens(self, obj):
#         refresh = RefreshToken.for_user(obj)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }

#     def validate_duplicate_user(self, data):
#         if User.objects.filter(user_rut=data['user_rut']).exists():
#             raise ValidationError("Rut already exists")
        
#         if User.objects.filter(user_phone=data['user_phone']).exists():
#             raise ValidationError("Phone already exists")
        
#         return data
    
#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         user = User.objects.create(**validated_data)
#         return user

class UserSerializer(serializers.ModelSerializer):
    user_role = serializers.SerializerMethodField()
    user_status = serializers.SerializerMethodField()
    tokens = serializers.SerializerMethodField()
    user_image = serializers.ImageField(required=False)
    id = serializers.ReadOnlyField()  # Asegúrate de incluir el campo `id`

    class Meta:
        model = User
        fields = '__all__'

    def get_user_role(self, obj):
        return f'{obj.user_role}'

    def get_user_status(self, obj):
        return "active" if obj.user_status == 1 else "not active"

    def get_tokens(self, obj):
        refresh = RefreshToken.for_user(obj)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def validate_duplicate_user(self, data):
        if User.objects.filter(user_rut=data['user_rut']).exists():
            raise ValidationError("Rut already exists")

        if User.objects.filter(user_phone=data['user_phone']).exists():
            raise ValidationError("Phone already exists")

        return data

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user
