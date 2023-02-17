## 利用Python製作ptt爬蟲程式
> 這是我跟著youtube影片練習的第一個Python網頁爬蟲  
> 使用Requests 函式庫來爬取Hahow課程資訊並將資料存至Excel中

## Code
* import 函式庫
```
import requests
from openpyxl import Workbook
```
* 爬取網頁  
Hahow 的課程資訊不是寫在html上 所以需要由Request分析  
1. 在hahow課程網頁中 開啟F12
1. 重新更新網頁
1. 開啟Network 分頁 尋找 course?page 這個request
1. 獲得這個request的 **Request URL**

## Links
[Youtube 教學來源-GrandmaCan -我阿嬤都會](https://www.youtube.com/watch?v=xua4Gno7xLo)

