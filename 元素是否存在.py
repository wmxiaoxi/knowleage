from selenium import webdriver
driver =webdriver.Chrome()
def is_ele_exist(ele):
    ss = driver.find_elements_by_id(ele)
    if len(ss) == 0:
         print("未找到元素")
         return False
    elif len(ss) == 1:
        return True
    else:
        print("找到%个元素", len(ss))
        return True




def is_ele_exist1(ele):
    try:
        driver.find_element_by_id(ele)
        return True
    except:
        return False


