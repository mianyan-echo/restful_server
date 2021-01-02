from rest_framework import serializers

from .models import IpCamera


class IpCameraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IpCamera
        fields = ['cam_id', 'geohash', 'dash_url', 'hls_url', 'online']
