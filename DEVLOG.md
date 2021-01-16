# api后端开发日志
***
***
## 2021.1.16
* 学着格式写了api-v1的api文档，正好也把之前预计的整个后端架构记录下来。
* 示意图
![avatar](https://github.com/mianyansanshengsanshi/restful_server/blob/master/templates/overall.jpg?raw=true)
* 目前RTMP推流使用的是打包好的ffmpeg，可以将任何视频流转码成rtmp流并推送到开启rtmp服务的nginx服务器
```shell
ffmpeg -f dshow -i video="EasyCamera" -vcodec h264_qsv -vprofile baseline -f flv -ar 44100 -ac 1 rtmp://192.168.56.102:1935/stream/87199a6c-2ad5-4f75-9215-42016882ea72
```
* geohash是基于经纬度，将地图**递归网格化**的地理表示算法（这个算法思想类似于**图像的算术编码压缩算法**），geohash这个算法来表示一个摄像头的位置的优缺点
  * 二维化一维，在数据库中直接设置12位的char就可以
  * 算法很简单容易实现，这样也可以实时的换算
  * 实现了地理查找与数据库查找的统一，可以灵活使用数据库的头匹配
  * 不用让数据库增加额外的geo扩展
  * 可以直接对接后期可能增加的redis等缓存中间件
  * 缺点是有一定的系统误差
* 关于nginx的反向代理，这个很常用，也可以消除跨域的问题。前端build好以后由nginx提供静态服务，只将对api的请求转发到django服务器上（这段中间应该还有uWSGI服务做转接）