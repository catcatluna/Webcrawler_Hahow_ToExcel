# 引入所需要的資源
import requests as req
# excel
from openpyxl import Workbook

# 開啟excel
wb=Workbook()
# 創新的excel資料表
ws =wb.active
# table 的title
title = ['課名','作者','價格','預購價','販售數']
# 加入excel table中
ws.append(title)

header ={
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
}
# 目標hahow 網頁中有2頁要獲取資料
for index in range(1,3):
    # 目標爬蟲網頁
    url ='https://api.hahow.in/api/group/music/courses?page='
    url = url+str(index)
    r = req.get(url,headers=header)
    # 將資料轉為json格式
    root_json =r.json()

    for data in root_json['data']:
        course = []
        course.append(data['title'])
        course.append(data['owner']['name'])
        course.append(data['price'])
        course.append(data['preOrderedPrice'])
        course.append(data['numSoldTickets'])
        ws.append(course)

#輸出excel檔案至同資料夾 檔名為coursedata
wb.save('coursedata.xlsx')