# 認識 RESTful API 📝

這篇文章將會簡單介紹 RESTful API ，希望大家會對 RESTful API 有更深入的了解 :blush:

如果有介紹不清楚或有錯誤的地方，歡迎大家 issuse 給我 :stuck_out_tongue_winking_eye:

* [Youtube Tutorial](https://youtu.be/gHCB0sd47Is)

## 介紹

REST，又稱為 Representational State Transfer，

全名為  Resource Representational State Transfer，中文可以翻成 具象狀態傳輸，

Resource : 資源

Representational : 像是 JSON，XML，YAML 等等......

State Transfer : 狀態傳輸。透過 HTTP 動詞實現 （ GET，POST，PUT，DELETE），

狀態可以定義成 Resource 的狀態，類似資料庫中 CRUD 操作後的結果。

以上看不懂沒關係，略懂即可，我知道很難懂 :fearful:

先給大家一個觀念，

***RESTful 是一種設計風格，或者說是一種設計規範***

**為什麼我們要使用 **RESTful API** ？ 用一般的 API 不行嗎？**

一般的 API 可能長得像這樣

* ***/api/get_file/ ( 得到檔案 )***

* ***/api/upload_file/ ( 新增檔案 )***

* ***/api/update_file/ ( 更新檔案 )***

* ***/api/delete_file/ ( 刪除檔案 )***

**RESTful API** 則長得像這樣

* ***/api/files/ ( GET -> 得到檔案 )***

* ***/api/files/ ( POST -> 新增檔案 )***

* ***/api/files/ ( PUT -> 更新檔案)***

* ***/api/files/ ( DELETE -> 刪除檔案 )***

溫馨小提醒 :heart:

不知道大家有沒有注意到我用複數，實務上用複數比較多。

從上面的比較可以發現，使用 **RESTful API** 我們只需要一個接口就可以完成 :open_mouth:，

並且我們透過 HTTP 不同的 method 達到相對應的功能。

**RESTful API** 讓我們以很優雅的方式顯示 Resource ( 資源 )，

Resource ( 資源 ) 是由 URI 來指定，

( URI 是什麼，這邊不詳細介紹，就麻煩大家 Google，可以先簡單想為 URL 是一種 URI 就好 :smile: )

對 Resource ( 資源 ) 的操作，包含取得、新增、修改和刪除資源，

這些操作剛好對應 HTTP 協定提供的 GET、POST、PUT 和 DELETE 方法 。

**RESTful API** 擁有清楚又簡短的 URI，可讀性非常強，舉個例子

```url
- GET /api/files/  得到所有檔案
- GET /api/files/1/  得到檔案 ID 為 1 的檔案
- POST /api/files/  新增一個檔案
- PUT /api/files/1/  更新 ID 為 1 的檔案
- PATCH /api/files/1/  更新 ID 為 1 的部分檔案內容
- DELETE /api/files/1/  刪除 ID 為 1 的檔案
```

上面做的事情就是 CRUD，那什麼是 CRUD ，也就是

Create（ 新增 ）、 Read（ 讀取 ）、 Update（ 更新 ）、 Delete（刪除）

溫馨小提醒 :heart:

特別來說明一下 PUT 和 PATCH，PUT 比較正確的定義是 Replace ( Create or Update )，

例如 PUT `/api/files/1/`  的意思是替換 `/api/files/1/`，假如已經存在就替換，如果沒有

也就新增，當然，新增的時候，必須包含必要的資料。

因為上面這個原因，大家會看到有時候使用 PUT 新增，也因為這個有點怪的行為，

所以又多了 PATCH 這個方法，可以用來做部分更新 ( Partial Update )。

或是我想搜尋檔案名稱為 hello 的檔案，**RESTful API** 可能為

```url
GET /api/files/search?key=hello
```

看到這邊，可以把 **RESTful** 想成是一種建立在 HTTP 協定之上的設計模式，充分的利用出 HTTP 協定的特定，

使用 URI 來表示資源，用各個不同的 HTTP 動詞（ GET、POST、PUT 和 DELETE 方法 ）來表示對資源的各種

行為，這樣做的好處就是資源和操作分離，讓對資源的管理有更好的規範以及前端（串接 API 或使用 API 的人）

可以很快速的了解你的 API ，省去很多不必要的溝通，如果熟悉 HTTP Method 的開發者，甚至可以不用看 API

文件就開始串接資料，當然，如果是更複雜的 API ，可能還是需要搭配文件，文件的撰寫可參考我之前寫的

[aglio_tutorial](https://github.com/twtrubiks/aglio_tutorial) 以及 [django_rest_framework_swagger_tutorial](https://github.com/twtrubiks/django_rest_framework_swagger_tutorial)。

這樣你現在是不是在想，**RESTful** 太神啦 :heart_eyes:

### Safe and Method Idempotent

GET 方法是安全方法，也就是不會對 Server 有修改，你只是讀取而已，

並不像 POST，PUT，DELETE，PATCH 這類的會修改資料。

 **Method Idempotent** （ 冪等方法 ），

他是什麼呢？ 簡單解釋，假設不考慮錯誤其他因素，若我們請求多次和單次

結果（ API 的 response ）是一樣的，就是 Method Idempotent。

像是 GET 就是 Method Idempotent，因為不管請求幾次，結果都是相同的；反之

，像是 POST 就不是 Method Idempotent ，原因是當我們發起第兩次 POST 時，

就會又新增一筆資料。

安全方法 和 Method Idempotent 可參考下面的表格

| HTTP | Method Idempotent | Safe |
| ------------------| ------ | ------ |
| OPTIONS | yes | yes |
| GET | yes | yes |
| HEAD | yes | yes |
| PUT | yes | no |
| POST | no | no |
| DELETE | yes | no |
| PATCH | no | no |

相信從上面這個表格，大家應該蠻好理解的，比較不好理解的可能就是，

為什麼 PATCH 不是 Method Idempotent，不是很好解釋  :sweat_smile:

我在這裡簡單解釋，PATCH 請求是會執行某個程序的，如果重複請求，

程序則可能多次執行，對 Server 端的資源就可能會造成額外的影響，所以

他不是 Method Idempotent。

如果大家想要更深入理解，麻煩大家 google :expressionless:

### RESTful API 缺點

記住，世界上沒有完美的東西，一定有他的缺點，

**RESTful** 很方便沒錯，但只要用戶了解了您的網站 URL 結構，就會開始產生 **安全性** 的問題

思考一個問題，一個用戶任意對你的 Database ( 資料庫 ) 操作 CRUD 是一件很可怕的事情 :scream:

再思考一個問題，假設我們得到一個使用者的 URL 是這樣 `/api/uesrs/1/`，一般來說使用者只

能存取自己的用戶資料，並不能查看別的用戶資料。否則，有心人可以嘗試從  `/api/uesrs/1/` 開

始 try 到 `/api/uesrs/100/` 得到其他的用戶資料。這是比較基本了問題，通常我們會先去驗證這個

使用者的身份，再來決定是否有權限可以存取用戶資料，所以我們一定要再處理對用戶進行身份

驗證和授權（可參考之前在 [django-rest-framework-tutorial](https://github.com/twtrubiks/django-rest-framework-tutorial#授權-authentications- ) 裡介紹的授權），然後使用 HTTPS。

再談談一個問題，現在很多都是前後端分離，通常我們會為了方便以 JSON 作為傳送的格式，但是

有時候可能會不小心把一些敏感的資訊送到前端，這樣就可能會導致資料外洩，或是有心人透過這

些資訊，去得到別人的資料以及有 **意思的** 訊息。所以當你在設計 API 時，一定要想想這些資訊洩

漏了會不會有什麼影響，如果有，可能資料需要再被加密之類的。

最後一個問題是實際面的問題，很多時候，我們的業務邏輯非常複雜，會導致如果要很嚴格的遵守

RESTful API  的規則，就不是那麼的好用，所以，有時候還是可以在 RESTful API  做一些修改，不一

定要那麼死死得遵守他的規則 :stuck_out_tongue:。

### 狀態碼

操作 API 的用戶，可以透過 HTTP 狀態碼了解一定的意思

HTTP status code 的常用情境如下 （ 通常，但不是絕對 ）

* 200 OK 用於請求成功 。GET 檔案成功，PUT， PATCH 更新成功

* 201 Created 用於請求 POST 成功建立資料。

* 204 No Content 用於請求 DELETE  成功。

* 400 Bad Request 用於請求 API 參數不正確的情況，例如傳入的 JSON 格式錯誤。

* 401 Unauthorized 用於表示請求的 API 缺少身份驗證資訊。

* 403 Forbidden 用於表示該資源不允許特定用戶訪問。

* 404 Not Found 用於表示請求一個不存在的資源。

更多詳細的可以參考 [HTTP Status Codes](http://www.restapitutorial.com/httpstatuscodes.html)

如果你的 API 比較複雜，還是要有文件記錄你的 error code 。

依據不同的 API 操作，定義適合的 HTTP 狀態碼和必要的錯誤資訊

（ 回傳一個 JSON 並且包含 error 屬性，error 這個屬性記錄錯誤訊息）。

## 結論

這次和大家簡單介紹了 **RESTful API** 的概念，基本上，還有很多可以研究，像是避免

API 被攻擊，可以考慮啟用 API 調用速率限制（ Rate limiting），又或是  HTTP Cache

的機制，最後，歡迎大家進入 **RESTful** 的世界 :laughing:
