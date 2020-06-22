from selenium import webdriver

option =webdriver.ChromeOptions()
option.add_argument('headless')
driver=webdriver.Chrome(chrome_option=option)

