from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.


class IpCamera(models.Model):
    # 从属用户，用于鉴权
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # 摄像头id,使用UUID V4生成伪随机的全局唯一标识
    cam_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # geohash
    # 可以方便的在数据库中根据geohash查询一个摄像头附近的摄像头
    # geohash长度>=10时精度误差就会降到1m以下
    geohash = models.CharField(max_length=12)

    # MPEG DASH直播流的url，实际浏览器或者代理服务器支持不到这么长的url
    # 此字段允许为空
    dash_url = models.URLField(max_length=65536, null=True, blank=True)

    # HLS直播流的url，实际浏览器或者代理服务器支持不到这么长的url
    # 此字段允许为空
    hls_url = models.URLField(max_length=65536, null=True, blank=True)

    # ffmpeg的拉流地址，也就是这个ip摄像头本来的地址
    # 也有可能不是URL
    src_url = models.CharField(max_length=65536)

    # 标志此摄像头是否在线
    online = models.BooleanField()

    # 修改时间
    date_change = models.DateTimeField(auto_now=True)

    class Meta:
        # 根据是否在线，修改时间找出最后被修改的在线摄像头
        get_latest_by = ['online', 'date_charge']

        # 表项按geohash排序
        # 映射到空间上是按Peano空间填充曲线排序
        # 这样方便根据geohash去查表
        ordering = ['geohash']

        # 索引列表,通过geohash索引
        indexes = [
            models.Index(fields=['geohash'], name='IpCam_geohash_idx')
        ]

# TODO: replay,保存回放相关的信息
