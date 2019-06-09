# django-rest-framework-tutorial

 Django-REST-framework 基本教學 - 從無到有 DRF-Beginners-Guide 📝

* [Youtube Tutorial PART 1 - 簡介](https://youtu.be/l9sq1DbVMAA)

因為 `Django > 2.0` 改動蠻多了，所以這邊會把一些和 `Django < 2.0` 不一樣的地方寫出來。

Django 以及 DRF 的版本請參考 [requirements.txt](https://github.com/twtrubiks/django-rest-framework-tutorial/blob/django2/requirements.txt)

```text
Django==2.2.1
djangorestframework==3.9.3
```

## 教學

建立 project ( 此步驟只須執行一次，所以不用在執行了 )

>django-admin startproject django_rest_framework_tutorial .

後面的 `.` 代表在目錄底下的意思。

### django-rest-framework 設定

***請記得要將 [Django-REST-framework](http://www.django-rest-framework.org/) 加入設定檔***

請在 [settings.py](https://github.com/twtrubiks/django-rest-framework-tutorial/blob/django2/django_rest_framework_tutorial/settings.py) 裡面的 **INSTALLED_APPS** 加入下方程式碼 (下圖)

```python
INSTALLED_APPS = (
    ...
    'rest_framework',
    ...
)
```
### 建立 Django App

建立一個 App ，

請在你的命令提示字元 (cmd ) 底下輸入

>python manage.py startapp musics

***建立完請記得要將 App 加入設定檔***

請在 [settings.py](https://github.com/twtrubiks/django-rest-framework-tutorial/blob/django2/django_rest_framework_tutorial/settings.py) 裡面的 **INSTALLED_APPS** 加入設定，

注意:exclamation:這邊和 `Django < 2.0` 不太一樣，

```python
INSTALLED_APPS = [
    .....
    'rest_framework',
    'musics.apps.MusicsConfig'
]
```

### Models

定義 [models.py](https://github.com/twtrubiks/django-rest-framework-tutorial/blob/django2/musics/models.py)

接著在命令提示字元 (cmd ) 底下輸入

> python manage.py makemigrations musics

> python manage.py migrate

### Serializers 序列化

定義 [serializers.py](https://github.com/twtrubiks/django-rest-framework-tutorial/blob/django2/musics/serializers.py)

### Views

定義 [views.py](https://github.com/twtrubiks/django-rest-framework-tutorial/blob/django2/musics/views.py)

### Routers 路由

注意:exclamation:這邊和 `Django < 2.0` 不太一樣。

定義 [django_rest_framework_tutorial/urls.py](https://github.com/twtrubiks/django-rest-framework-tutorial/blob/django2/django_rest_framework_tutorial/urls.py)，

基本上就是改成使用 `path`，

```python
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from musics.views import MusicViewSet

router = DefaultRouter()
router.register('musics', MusicViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    # for rest_framework
    path('api/', include(router.urls)),
    # for rest_framework auth
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

### Extra actions for routing

注意:exclamation:這邊和 `Django < 2.0` 不太一樣。

在 `Django < 2.0` 時，是使用 `@detail_route` 和 `@list_route`。

但在 `Django > 2.0`中，統一都使用 `@action` decorator

搭配 detail argument 參數 ( `True` or `False`)。

範例程式碼可參考 [views.py](https://github.com/twtrubiks/django-rest-framework-tutorial/blob/django2/musics/views.py)

`@action` decorator 搭配 `detail=True` ( 就是以前的 `@detail_route` )

```python
# [GET] /api/musics/{pk}/detail/
@action(detail=True, methods=['get'], url_path='detail')
def detail_action(self, request, pk=None):
    music = get_object_or_404(Music, pk=pk)
    result = {
        'singer': music.singer,
        'song': music.song
    }
    return Response(result, status=status.HTTP_200_OK)
```

以上面這個例子來說， URL pattern 為 `/api/music/{pk}/detail/`。

`@action` decorator 搭配 `detail=False` ( 就是以前的 `@list_route` )

```python
# [GET] /api/musics/all_singer/
@action(detail=False, methods=['get'], url_path='all_singer')
def all_singer(self, request):
    music = Music.objects.values_list('singer', flat=True).distinct()
    return Response(music, status=status.HTTP_200_OK)
```

以上面這個例子來說，URL pattern 為 `/api/music/all_singer/`。

更多資訊可參考 [https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing](https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing)。

## 後記

這篇 Django > 2.0 的文章，我會慢慢更新，如果我發現一些寫法或功能，我會更新在這篇。

## 執行環境

* Python 3.6.6

## Reference

* [Django](https://www.djangoproject.com/)
* [Django-REST-framework](http://www.django-rest-framework.org/)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
