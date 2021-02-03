from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import IpCameraViewSet


router = routers.DefaultRouter()
router.register(r'ipcameras', IpCameraViewSet, basename='ipcamera')

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth-token', views.obtain_auth_token),
]
