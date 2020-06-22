from selenium import webdriver
import time
import unittest
driver=webdriver.Chrome()
try:
    driver.find_element_by_id("ed")
except:
    print()
    nowtime=time.strftime("%Y%m%d.%H.%M.%S")
    nowtime1=time.localtime()
    driver.get_screenshot_as_file('%s.png'%nowtime)