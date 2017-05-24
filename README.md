# django-rest-framework-tutorial

 Django-REST-framework 基本教學 - 從無到有 DRF-Beginners-Guide 📝

* [Youtube Tutorial PART 1](https://youtu.be/lunVXqMVsrs)
* [Youtube Tutorial PART 2](https://youtu.be/Qnir5iFpMyQ)

透過 [Django REST framework](http://www.django-rest-framework.org/) ( DRF ) 建立 REST API 非常方便快速，

在這裡教大家建立自己的第一個 [Django-REST-framework](http://www.django-rest-framework.org/)  :smile:

建議對 [Django](https://github.com/django/django) 還不熟的人，可以先閱讀我之前寫的 [Django 基本教學 - 從無到有 Django-Beginners-Guide](https://github.com/twtrubiks/django-tutorial)，

先建立一些基本觀念，再來看 DRF 會比較清楚。

## 教學

請先確認電腦有安裝 [Python](https://www.python.org/)

請在你的命令提示字元 (cmd ) 底下輸入

安裝 [Django](https://github.com/django/django)

>pip install django

安裝 [Django-REST-framework](http://www.django-rest-framework.org/)
>pip install djangorestframework

基本上安裝應該沒什麼問題。

### django-rest-framework 設定

***請記得要將 [Django-REST-framework](http://www.django-rest-framework.org/) 加入設定檔***

請在 settings.py 裡面的 **INSTALLED_APPS** 加入下方程式碼 (下圖)

```python
INSTALLED_APPS = (
    ...
    'rest_framework',
    ...
)
```

![alt tag](http://i.imgur.com/bm7cO0e.jpg)

### 建立 Django App

先建立一個觀念，在 [Django](https://github.com/django/django) 中，通常我們會依照 **功能** 去建議一個 App ， 例如範例的 musics ，代表他是 管理音樂 的部份。

有了這個觀念之後，我們動手開始做吧～

請在你的命令提示字元 (cmd ) 底下輸入

>python manage.py startapp musics

***建立完請記得要將 App 加入設定檔***

請在 settings.py 裡面的 **INSTALLED_APPS** 加入 musics (也就是你自己建立的 App 名稱)

![alt tag](http://i.imgur.com/xP1MoFI.jpg)

### Models

定義出資料庫中的結構（schema），並且透過 Django 中的指令去建立資料庫。

[Django](https://github.com/django/django) 預設是使用 [SQLite](https://www.sqlite.org/) ，如果想要修改為其他的資料庫，可以在 settings.py  裡面進行修改。

首先，請先在 models.py 裡面增加下方程式碼 (下圖)

```python
from django.db import models


# Create your models here.
class Music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"

```

![alt tag](http://i.imgur.com/gydF0x4.jpg)

接著在命令提示字元 (cmd ) 底下輸入

>python manage.py makemigrations

![alt tag](http://i.imgur.com/xH4Sm3s.jpg)

> python manage.py migrate

![alt tag](http://i.imgur.com/CpcdT3X.jpg)

makemigrations ： 會幚你建立一個檔案，去記錄你更新了哪些東西。

migrate ： 根據 makemigrations 建立的檔案，去更新你的 DATABASE 。

執行完上面的指令之後，

你可以使用[SQLiteBrowser](http://sqlitebrowser.org/) 或  [PyCharm](https://www.jetbrains.com/pycharm/) 觀看 DATABASE，

你會發現多出一個 **music** 的 table ( 如下圖 )

![alt tag](http://i.imgur.com/xVbTtjq.jpg)

有沒有注意到我們明明在 models.py 裡面就沒有輸入 id ，可是 database 裡面卻有 id 欄位，

這是因為 Django 預設會幫你帶入，所以可以不用設定。

### Serializers 序列化

Serializers 序列化 是 DRF 很重要的一個地方 :star:

主要功能是將 Python 結構序列化為其他格式，例如我們常用的 JSON。

在 musics 裡面新增 serializers.py，並輸入下方程式碼

```python
from rest_framework import serializers
from musics.models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created')

```

![alt tag](http://i.imgur.com/KY5UwHW.jpg)

如果你想要全部 fields ，可以使用第 8 行的寫法。

### Views

在  [Django 基本教學 - 從無到有 Django-Beginners-Guide](https://github.com/twtrubiks/django-tutorial) 中我們使用 views，

而在 DRF 中提供我們可以使用另一種稱為 viewsets 。

請在 views.py 裡輸入下方程式碼 (下圖)

```python
# Create your views here.
from musics.models import Music
from musics.serializers import MusicSerializer

from rest_framework import viewsets


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

```

![alt tag](http://i.imgur.com/GMSz7u7.jpg)

只需要寫這樣，你就擁有 CRUD 的全部功能，是不是非常強大 :open_mouth:

為什麼呢? 因為 DRF 的 **viewsets.ModelViewSet** 裡面幫你定義了這些功能，

![alt tag](http://i.imgur.com/GHbUOT5.jpg)

當然，如果你需要，也可以覆寫他。

### Routers 路由

DRF 提供 DefaultRouter 讓我們快速建立 Routers 路由。

請先將 urls.py 裡面增加一些程式碼，如下圖

```python
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from musics import views

router = DefaultRouter()
router.register(r'music', views.MusicViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]

```

![alt tag](http://i.imgur.com/imdF1f8.jpg)

最後執行 Django ， 然後瀏覽   [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

你應該會看到如下圖

![alt tag](http://i.imgur.com/ZpmiVnG.jpg)

恭喜你，成功了 :smile:

接下來，讓我來測試 API 吧~

### 測試 API

在測試 API 之前，大家必須先了解一下什麼是 REST API

REST API 全名為 RESTful API，它並不是一個新東西、新技術，它只是一個規範。

簡單說明 :

GET : 讀取資源

PUT : 替換資源

DELETE : 刪除資源

POST : 新增資源

PATCH : 更新資源部份內容

剩下更詳細的資料就麻煩大家 GOOGLE了，我在現在來 測試 API   :smiley:

測試 API 的工具很多，在這裡我們使用 [Postman](https://www.getpostman.com/) ，大家可以用自己習慣的工具。

#### POST

我們先來新增幾筆資料，如下圖

![alt tag](http://i.imgur.com/zalPhwM.jpg)

在 步驟1 的地方輸入你的 API 的網址，範例為  [http://127.0.0.1:8000/api/music/](http://127.0.0.1:8000/api/music/)

在 步驟2 body 的地方，填入 song 和 singer 的值，然後按下 Send，

接著看 response ( 步驟3 )，也就是你新增進去 dabase 的資料。

#### GET

如果你想一次看裡面全部的資料，可以使用 [http://127.0.0.1:8000/api/music/](http://127.0.0.1:8000/api/music/)

![alt tag](http://i.imgur.com/clilnZL.jpg)

或是你只想看特定的某一筆，可以使用 [http://127.0.0.1:8000/api/music/2/](http://127.0.0.1:8000/api/music/2/)

![alt tag](http://i.imgur.com/RHwAjpU.jpg)

#### PUT

如果你想修改特定資料，可以使用 [http://127.0.0.1:8000/api/music/2/](http://127.0.0.1:8000/api/music/2/)

![alt tag](http://i.imgur.com/7v5U03P.jpg)

當按下 send 之後，會看到 response ( 步驟3 )的地方回傳修改後的值。

#### DELETE

如果你想刪除特定資料，可以使用 [http://127.0.0.1:8000/api/music/3/](http://127.0.0.1:8000/api/music/3/)

![alt tag](http://i.imgur.com/HjCCICb.jpg)

執行後，你會發現 id=3 的資料被刪除了。

![alt tag](http://i.imgur.com/tOQS5cq.jpg)

### 授權 (Authenticaions )

在 REST API 中，授權很重要，如果沒有授權，別人一直任意不受限制的操作你的 API ，很危險，

所以 DRF 有提供 Authenticaions，讓我們來試試看吧~

首先，請在 views.py 裡面新增  permission_classes

```python
# Create your views here.
from musics.models import Music
from musics.serializers import MusicSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,)
```

![alt tag](http://i.imgur.com/RbQrZLt.jpg)

接著在 urls.py 裡面增加 api-auth

```python
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from musics import views

router = DefaultRouter()
router.register(r'music', views.MusicViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

![alt tag](http://i.imgur.com/YISdOvo.jpg)

最後執行 Django ， 然後瀏覽   [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) ，你會發現右上角多了 Log in 的按鈕

![alt tag](http://i.imgur.com/DxgSK9q.jpg)

我們先使用我們在 [Django 基本教學 - 從無到有 Django-Beginners-Guide](https://github.com/twtrubiks/django-tutorial) 裡面學到的 建立超級使用者

>python manage.py createsuperuser

![alt tag](http://i.imgur.com/wqacaCR.jpg)

讓我們再次使用 POSTMAN，我們用 GET 當作範例

#### GET 授權

![alt tag](http://i.imgur.com/MoMLRB3.jpg)

有注意到嗎? response 說我沒有 授權，

所以這時候我們就必須再加上授權才能操作 API (如下圖)，我們可以操作 API 了

我的 帳號/密碼 設定為 twtrubiks/password123

![alt tag](http://i.imgur.com/8leY8ZH.jpg)

恭喜你，基本上到這裡，已經是一個非常簡單的  [Django-REST-framework](http://www.django-rest-framework.org/) ，趕快動手下去玩玩吧 :stuck_out_tongue:

也可以觀看下一個範例

DataTables (server-side) 搭配 Django REST framework 簡單範例

[DRF-dataTable-Example-server-side](https://github.com/twtrubiks/DRF-dataTable-Example-server-side)

## 執行環境

* Python 3.4.3

## Reference

* [Django](https://www.djangoproject.com/)
* [Django-REST-framework](http://www.django-rest-framework.org/)

## License

MIT license
