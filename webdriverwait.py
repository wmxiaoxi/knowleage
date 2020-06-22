from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
driver=webdriver.Chrome()
WebDriverWait(driver,10).until(lambda x:x.find_by_id(''))
