# #浏览器的操作

# driver.refresh()
# driver.forward()
# driver.back()
# driver.set_window_size(500,980)
# driver.maximize_window()
# driver.minimize_window()
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_file("d:\\test\\1.jpg")
# driver.close()#关闭部分窗口
# driver.quit()#关闭进程，所有窗口

# #元素定位
# driver.find_element_by_id()
# driver.find_element_by_name()
# driver.find_element_by_class_name()
# driver.find_element_by_xpath()
# driver.find_element_by_css_selector()
# driver.find_element_tag_name()
# driver.find_element_by_link_text()
# driver.find_element_by_partial_link_text()

# #xpath定位,没有id name xpath可以用其他属性来定位
# driver.find_element_by_xpath("//*[@id='kw']") #xpath id name  class 定位
# driver.find_element_by_xpath("//input[@id='kw']")#标签定位
# driver.find_element_by_xpath("//form[@id='form']/span/input")#层级定位,先定位到爸爸再往下定位；先定位到爷爷 在往下定位；
# driver.find_element_by_xpath("//select[@id='nr'/option[1]]")#一个父亲生的，多胞胎兄弟，则索引定位,这里的索引从1开始
# driver.find_element_by_xpath("//*[@id='kw'&@autocomplete='off']")#xpath逻辑运算
# driver.find_element_by_xpath("//*[contains(text(),'hao123')]")#xpath模糊匹配，比如hao123
# driver.find_element_by_xpath("//*[starts-with(@id,'ueditor_')]")
# driver.find_element_by_xpath("//*[ends-with(@id,'ueditor_')]")
# driver.find_element_by_xpath("//*[contains(@id,'kw')]")
# driver.find_element_by_xpath("//*[matchs(text(),'hao123')]")
#
# #css标签 id  class定位
# driver.find_element_by_css_selector('#kw')##号表示id; .表示class;css直接用标签名称，无任何标示符
# driver.find_element_by_css_selector('.s_ipt')
# driver.find_element_by_css_selector('input')
# #css其他定位
# driver.find_element_by_css_selector("[name='wd']")
# #css可以通过标签和属性组合来定位
# driver.find_element_by_css_selector("input#kw")
# #层级定位
# driver.find_element_by_css_selector("form#form>span>input")
# #索引定位
# driver.find_element_by_css_selector('select#nr>option:nth child=(1)')
# #逻辑运算定位
# driver.find_element_by_css_selector("input[id='kw'][name='wd']")

# ##sbumit()一般用于模拟回车键
# from selenium.webdriver.common.keys import Keys
# driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys(Keys.ENTER)
# driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys(Keys.CONTROL,'c')
# driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys(Keys.TAB)

#鼠标悬停


# #checkbox
# checkboxs=driver.find_elements_by_xpath(".//*[@type='checkbox']")
# for i in checkboxs:
#     i.click()
#
# #是否被选中
# r=driver.find_element_by_id("kw").is_selected()

# #js处理日历的只读属性
# js='document.getElementById('').removeAttribute("reaaonly")'
# driver.execute_script(js)


#
# #table定位
# driver.find_element_by_xpath('.//*[@id="table”/tr[2]/td[1]]')