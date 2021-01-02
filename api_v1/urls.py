from django.urls import path, include
from rest_framework import routers

from .views import IpCameraViewSet


router = routers.DefaultRouter()
router.register(r'ipcameras', IpCameraViewSet, basename='ipcamera')

urlpatterns = [
    path('', include(router.urls)),
]
