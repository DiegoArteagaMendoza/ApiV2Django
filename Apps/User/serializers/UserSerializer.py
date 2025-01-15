from Apps.User.models.UserModel import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    user_role = serializers.SerializerMethodField()
    user_status = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = '__all__'
    
    def get_user_role(self, obj):
        return f'{obj.user_role}'
    
    def get_user_status(self, obj):
        return "active" if obj.user_status == 1 else "not active"

    def validate_duplicate_user(self, data):
        if User.objects.filter(user_rut=data['user_rut']).exists():
            raise ValidationError("Rut already exists")
        
        if User.objects.filter(user_phone=data['user_phone']).exists():
            raise ValidationError("Phone already exists")
        
        return data
    
    def create(self, validated_data):
        validated_data['user_password'] = make_password(validated_data['user_password'])
        user = User.objects.create(**validated_data)
        if user:
            return user
        else:
            return None