# Django Rest Framework api服务器
***
## 依赖
```
Python              3.8.5
    asgiref             3.3.1
    Django              3.1.4
    django-filter       2.4.0
    djangorestframework 3.12.2
    sqlparse            0.4.1
```
***
# 初始化
```shell
python -m venv venv
./venv/Scripts/activate

pip install -r requirements.txt
```
***
## 启动
```shell
python manage.py runserver 0.0.0.0:8000
```
***
目前在更新v1版本，api文档见[api_v1/README.md](https://github.com/mianyansanshengsanshi/restful_server/blob/master/api_v1/README.md)
可配合前端 [vue_screen](https://github.com/mianyansanshengsanshi/vue_screen) 使用