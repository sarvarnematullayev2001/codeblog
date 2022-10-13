# Rest Framework
from rest_framework.response import Response
from rest_framework import status

# Models
from user.models import User


def signup(first_name, last_name, email, date_of_birth, password):
    check_email = User.objects.filter(email=email).exists()
    if check_email is True:
        return Response({'detail': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    create_user(first_name, last_name, email, date_of_birth, password)
    return Response({'detail': 'successfully registered'}, status=status.HTTP_201_CREATED)


def create_user(
        first_name: str,
        last_name: str,
        email: str,
        date_of_birth: str,
        password=None
):
    user = User.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        date_of_birth=date_of_birth,
        is_active=True,
        is_staff=False,
        is_superuser=False,
    )
    if password:
        user.set_password(password)
        user.save()
    return user