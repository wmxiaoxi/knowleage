from  selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://i.meituan.com/account/login?backurl=http%3A%2F%2Fpiaofang.maoyan.com%2F%3Fver%3Dnormal")
print(driver.get_cookies())


driver.get_cookie()  ##获取指定cookie
driver.delete_cookie()###删除指定cookie
driver.delete_all_cookies()

c1 = {u'domain': u'.cnblogs.com',
      u'name': u'.CNBlogsCookie',
      u'value': u'xxxx',
      u'expiry': 1491887887,
      u'path': u'/',
      u'httpOnly': True,
      u'secure': False}

c2 = {u'domain': u'.cnblogs.com',
      u'name': u'.Cnblogs.AspNetCore.Cookies',
      u'value': u'xxxx',
      u'expiry': 1491887887,
      u'path': u'/',
      u'httpOnly': True,
      u'secure': False}

driver.add_cookie(c1)  # 添加2个值
driver.add_cookie(c2)
# 刷新下页面就见证奇迹了
driver.refresh()



# cookie ={u'domain': u'.cnblogs.com',
#             u'name': u'.CNBlogsCookie',
#             u'value': u'xxxx',
#             u'expiry': 1491887887,
#             u'path': u'/',
#             u'httpOnly': True,
#             u'secure': False}
#
# name：cookie的名称
#
# value：cookie对应的值，动态生成的
#
# domain：服务器域名
#
# expiry：Cookie有效终止日期
#
# path：Path属性定义了Web服务器上哪些路径下的页面可获取服务器设置的Cookie
#
# httpOnly：防脚本攻击
#
# secure:在Cookie中标记该变量，表明只有当浏览器和Web Server之间的通信协议为加密认证协议时，
#
# 浏览器才向服务器提交相应的Cookie。当前这种协议只有一种，即为HTTPS。