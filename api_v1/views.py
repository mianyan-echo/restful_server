from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .models import IpCamera
from .serializers import IpCameraSerializer

# Create your views here.


class IpCameraViewSet(viewsets.ModelViewSet):
    # queryset = IpCamera.objects.all()
    serializer_class = IpCameraSerializer

    def get_queryset(self):
        _geohash = self.request.query_params.get('geohash', None)
        _range = self.request.query_params.get('range', '')
        if _geohash:
            if _range.isdigit() and _geohash > int(_range):
                _range = int(_range)
                queryset = IpCamera.objects.filter(geohash__startswith=_geohash[:len(_geohash)-_range])
            else:
                queryset = IpCamera.objects.filter(geohash=_geohash)
            return queryset
        return IpCamera.objects.all()
