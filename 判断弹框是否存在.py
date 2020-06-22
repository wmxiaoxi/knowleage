from selenium import webdriver
driver=webdriver.Chrome()
def is_alert_exists():
    try:
        alert=driver.switch_to.alert
        alert.text
        return alert
    except :
        return False
