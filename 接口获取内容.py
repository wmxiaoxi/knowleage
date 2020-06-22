# coding:utf-8
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


par={"type":"DAILY","date":"2020-03-11","t":"1583994172905","category":"DRAMA"}
h={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36","Accept":"application/json","Content-Type":"application/json;charset=UTF-8","Accept-Encoding":"gzip, deflate"
}
s=requests.session()
r=s.get("http://data.guduodata.com/show/datalist",params=par,headers=h)
body=r.json()
list=[]
#print(body['data'])
#print(body['data'])

for i in range(0,len(body['data'])-1):
    list = []
    resp1=body['data'][i]
    #print(resp1)
    list.append(body['data'][i]['platforms'])
    list.append(body['data'][i]['show_id'])
    list.append(body['data'][i]['name'])
    print(list)

# list=[]
# for i in range(0,len(body['data'])-1):
#   r= body['data'][i]["name"]
#   c=body['data'][i]['platforms']
#   list.append(r)
#   list.append(c)
# print(list)











