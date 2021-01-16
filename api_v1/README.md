# api_v1文档
***
## 所有监控列表
<details>
<summary>详细信息</summary>

* 简要描述
  * 获取所有上线过的ip摄像头的状态信息
* 请求URL
  * `/api-v1/ipcameras/`
* 请求方式
  * GET
* 参数
  * 这两个参数一起提供，可以以一个geohash为原点，搜寻周围range范围内的所有连接过的摄像头。
  * 如给定一长12位的geohash，range为5，则会在数据库中匹配所有geohash的前7位，返回匹配到的摄像头列表。

| 参数名  | 必选 | 类型   | 说明                          |
| ------- | ---- | ------ | ----------------------------- |
| geohash | 否   | string | 搜索范围原点的geohash         |
| range   | 否   | int    | 对于原点geohash的模糊搜索位数 |

* 返回示例
  * `GET /api-v1/ipcameras/`
```json5
[
    {
        "cam_id": "24e307e3-f5da-45ce-a2d4-c74ccbf37a39",
        "geohash": "wx4g09n5duw1",
        "online": false
    },
    {
        "cam_id": "87199a6c-2ad5-4f75-9215-42016882ea72",
        "geohash": "wx4g09n7gs4u",
        "online": true
    }
]
```
  * `GET /api-v1/ipcameras/?geohash=wx4g09n7gs4u&range=4`
```json5
[
    {
        "cam_id": "87199a6c-2ad5-4f75-9215-42016882ea72",
        "geohash": "wx4g09n7gs4u",
        "online": true
    }
]
```
</details>

## 某一监控的URL信息
<details>
<summary>详细信息</summary>

* 简要描述
  * 获取某一监控的MPEG DASH、HLS、源地址等直播流地址
* 请求URL
  * `/api-v1/ipcameras/{cam_id}`
* 请求方式
  * GET
* 参数
  * 可选`dash_url`,`hls_url`,`cam_id`,`geohash`,`online`
  * 不选返回全部信息

| 参数名 | 必选 | 类型   | 说明                        |
| ------ | ---- | ------ | --------------------------- |
| entry  | 否   | string | 要具体返回的某一项直播源url |

* 返回示例
  * `GET /api-v1/ipcameras/87199a6c-2ad5-4f75-9215-42016882ea72`
```json5
{
    "cam_id": "87199a6c-2ad5-4f75-9215-42016882ea72",
    "geohash": "wx4g09n7gs4u",
    "dash_url": "http://192.168.56.102/dash/87199a6c-2ad5-4f75-9215-42016882ea72.mpd",
    "hls_url": "http://192.168.56.102/hls/87199a6c-2ad5-4f75-9215-42016882ea72.hls",
    "online": true
}
```
  * `GET /api-v1/ipcameras/87199a6c-2ad5-4f75-9215-42016882ea72/?entry=dash_url`
```json5
{
    "cam_id": "87199a6c-2ad5-4f75-9215-42016882ea72",
    "dash_url": "http://192.168.56.102/dash/87199a6c-2ad5-4f75-9215-42016882ea72.mpd"
}
```
</details>