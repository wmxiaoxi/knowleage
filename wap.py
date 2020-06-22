# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.chrome.options import Options

url = "https://login.m.taobao.com/msg_login.htm?spm=0.0.0.0"

# 设置成手机模式
mobile_emulation = {"deviceName":"iPhone 6"}
options =webdriver.ChromeOptions()
options.add_experimental_option('w3c',  False)
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options=options)

driver.get(url)

driver.find_element_by_id("username").send_keys("yoyoketang")

# 触摸事件
el = driver.find_element_by_xpath("//*[@id='getCheckcode']")
TouchActions(driver).tap(el).perform()
el.click()