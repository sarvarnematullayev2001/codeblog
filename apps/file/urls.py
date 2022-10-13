# Django
from django.urls import path, include

# Rest-Framework
from rest_framework.routers import DefaultRouter

# Project
from file.views import (
    FileViewSet
)

router = DefaultRouter()
router.register('', FileViewSet, 'files')

urlpatterns = router.urls