# Rest Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Django
from django.contrib.auth import authenticate

# Project
from user.models import User


def login(email, password, is_superuser=False):
    invalid_email_or_password = 'invalid_email_or_password'
    activate_error = 'please_activate_your_account'
    
    try:
        if '@' in email and User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
        else:
            return Response({'detail': invalid_email_or_password}, status=status.HTTP_400_BAD_REQUEST)
        if user.is_active is False:
            return Response({'detail': activate_error}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(email=user.email, password=password)
        if user is None:
            return Response({'detail': invalid_email_or_password}, status=status.HTTP_400_BAD_REQUEST)
        if is_superuser is True and user.is_superuser is False:
            return Response({'detail': 'access denied'}, status=status.HTTP_400_BAD_REQUEST) 
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'detail': invalid_email_or_password}, status=status.HTTP_400_BAD_REQUEST)