from Apps.User.models.UserModel import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    user_role = serializers.SerializerMethodField()
    user_status = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['id', 'user_name', 'user_last_name', 'user_email', 'user_phone', 'user_role', 'user_status']
    
    def get_user_role(self, obj):
        return f'{obj.user_role}'
    
    def get_user_status(self, obj):
        return "active" if obj.user_status == 1 else "not active"

    def validate_duplicate_user(self, data):
        if User.objects.filter(user_rut=data['user_rut']).exists():
            raise serializers.ValidationError("Rut alredy exist")
        
        if User.objects.filter(user_phone=data['user_phone']).exists():
            raise serializers.ValidationError("Phone alredy exist")
        
        return data
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)