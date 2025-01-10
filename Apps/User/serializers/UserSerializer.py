from ..models import UserModel as User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    user_role = serializers.SerializerMethodField()
    user_status = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'user_name', 'user_last_name', 'user_email', 'user_phone', 'user_role', 'user_status']
    
    def get_user_role(self, obj):
        return f'User role: {obj.user_role}'
    
    def get_user_status(self, obj):
        return "User status: active" if obj.user_status == 1 else "User status: not active"

    def validate_duplicate_user(self, data):
        if User.objects.filter(user_email=data['user_email']).exists():
            raise serializers.ValidationError("Email alredy exist")
        
        if User.objects.filter(user_phone=data['user_phone']).exists():
            raise serializers.ValidationError("Phone alredy exist")
        
        return data
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)