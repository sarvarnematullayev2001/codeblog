# Rest Framework
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics


# Project
from .serializers import SignUpSerializer, LoginSerializer, UserSerializer
from .services.signup import signup
from .services.login import login
from .models import User

# Django
from django.shortcuts import get_object_or_404


class SignUpAPIView(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return signup(**serializer.validated_data)


class LoginAPIView(APIView):
    
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return login(**serializer.validated_data)


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)