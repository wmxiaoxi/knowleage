# coding:utf-8
import requests

# 作者：上海-悠悠 QQ群：588402570
url = 'http://www.xxx.com/xxx/xxx?begNy=&endNy='
herder = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Cookie": "你抓到的cookies",
            "Connection": "keep-alive"
          }

r = requests.get(url, headers=herder)

# open打开excel文件，报存为后缀为xls的文件
fp = open("yoyo.xls", "wb")
fp.write(r.content)
fp.close()