#coding:utf-8
import  requests
url="http://httpbin.org/post"
body='<?xml version="1.0" encoding = "UTF-8"?>' \
       '<COM>' \
       '<REQ name="上海-悠悠">' \
       '<USER_ID>yoyoketang</USER_ID>' \
       '<COMMODITY_ID>123456</COMMODITY_ID>' \
       '<SESSION_ID>absbnmasbnfmasbm1213</SESSION_ID>' \
       '</REQ>' \
       '</COM>'


r=requests.post(url,data=body.encode('utf-8'))
print(r.txt)






# coding:utf-8
import requests
# 作者：上海-悠悠 QQ交流群：588402570

url = "http://httpbin.org/post"

# xml格式body
with open("body1_xml", encoding="utf-8") as fp:
    body = fp.read()
print(body)


# 遇到编码报错时候，对body进行encode
r = requests.post(url, data=body.encode("utf-8"))

print(r.text)

