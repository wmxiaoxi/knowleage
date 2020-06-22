from  selenium import webdriver
import re#非贪婪模式findall方法返回的是一个list集合

driver=webdriver.Chrome()



###案例-
driver.get("http://www.cnblogs.com/yoyoketang/")
page=driver.page_source
#非贪婪模式匹配，re.S
url_list=re.findall("herf=\'(.*?)\'",page,re.S)
url_all=[]
for url in url_list:
    if "http" in url:
        print(url)
        url_all.append(url)
print(url_all)





###案例2








