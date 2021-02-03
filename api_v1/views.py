from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .models import IpCamera
from .serializers import IpCameraSerializer
from .permissions import TokenIsOwnerAndReadOnly

# Create your views here.


class IpCameraViewSet(viewsets.ModelViewSet):
    # queryset = IpCamera.objects.all()
    serializer_class = IpCameraSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (TokenIsOwnerAndReadOnly, )

    def get_queryset(self):
        # 获取归用户所有的ip摄像头
        owner = self.request.user
        owner_cameras = owner.ipcamera_set

        _geohash = self.request.query_params.get('geohash', None)
        _range = self.request.query_params.get('range', '')
        if _geohash:
            if _range.isdigit() and len(_geohash) > int(_range):
                _range = int(_range)
                queryset = owner_cameras.filter(geohash__startswith=_geohash[:len(_geohash)-_range])
            else:
                queryset = owner_cameras.filter(geohash=_geohash)
            return queryset
        return owner_cameras.all()

    # 目前这两个是临时写法，实际项目开发中这么写会变得极不好维护，
    # 实际应采用framework自带的过滤器、筛选器、查找器
    # 最本质的改法是直接分表，将dash_url、hls_url、src_url单独分为一个‘一对多’表
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # 暂时不需要分页
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        data = []
        for query in queryset:
            data.append({'cam_id': query.cam_id,
                         'geohash': query.geohash,
                         'online': query.online})
        # serializer = self.get_serializer(queryset, many=True)
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        """
        根据传入的url参数定制返回的条目
        """
        instance = self.get_object()
        entry = self.request.query_params.get('entry')
        if entry:
            try:
                entry_data = getattr(instance, entry)
            except AttributeError:
                raise Http404
            return Response({'cam_id': instance.cam_id,
                             entry: entry_data})
        else:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
