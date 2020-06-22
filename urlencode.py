import requests
from urllib.parse import urlencode, quote, unquote
#
# url = "http://www.example.com/"
# par = {
#     "a": "上海",
#     "b": "悠悠"
# }
# body = {
#     "content": "悠悠",
#     "charsetSelect": "utf-8",
#     "en": "UrlEncode编码"
# }
#
# r = requests.post(url, params=par, data=body)
# print(r.url)
#
#




#
# from urllib.parse import urlencode, quote, unquote
#
# # urlencode方法参数是字典
#
# body = {
#     "content": "悠悠",
#     "charsetSelect": "utf-8",
#     "en": "UrlEncode编码"
# }
# print(urlencode(body))




# # quote方法参数是字符串
#
# print(quote("上海-悠悠"))
# url = "http://www.example.com/?a=上海&b=悠悠"
# print(quote(url))










import requests
from urllib.parse import urlencode, quote, unquote

url = "http://www.example.com/"
par = {
    "a": "上海",
    "b": "悠悠"
}
body = {
    "content": "悠悠",
    "charsetSelect": "utf-8",
    "en": "UrlEncode编码"
}

r = requests.post(url, params=par, data=body)
print(r.url)
print(unquote(r.url))
r.elapsed.total_seconds()    #这是响应时间


# r = requests.post(url, params=par, data=body,timeout=1)    #如果响应时间超过了1s 则超时

