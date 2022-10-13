# Django
from django.urls import path

# Project
from .views import SignUpAPIView, LoginAPIView, ProfileAPIView


urlpatterns = [
    path('signup/', SignUpAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),
]
