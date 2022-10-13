from rest_framework import serializers
from  .models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'linkedin', 'phone_number', 'date_of_birth']
        read_only_fields = ['is_active', 'is_admin', 'is_staff']


class SignUpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()