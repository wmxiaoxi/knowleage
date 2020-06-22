from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from tomorrow import threads
import pytest
# logger=Logger(logger="method").getlog()
# exc_info = 1
import time
class Test_method():

    # option=webdriver.ChromeOptions()
    # option.add_argument('headless')
    # driver = webdriver.Chrome(chrome_options=option)    ##静默模式

    #driver=webdriver.Chrome()
    # driver=webdriver.Firefox()

    # @pytest.fixture()
    # @pytest.mark.parametrize('name',['Chrome'])
    # def startBrowser(self,name):
    #     try:
    #         if name == "firefox" or name == "Firefox" or name == "ff":
    #             driver = webdriver.Firefox()
    #             return driver
    #         elif name == "chrome" or name == "Chrome":
    #             driver = webdriver.Chrome()
    #             return driver
    #         else:
    #             print("Not found this browser,You can use 'firefox', 'chrome', 'ie' or 'phantomjs'")
    #     except Exception as msg:
    #         print("启动浏览器出现异常：%s" % str(msg))
    def start(self,name):
        try:
            if name == "firefox" or name == "Firefox" or name == "ff":
                driver = webdriver.Firefox()
                return driver
            elif name == "chrome" or name == "Chrome":
                driver = webdriver.Chrome()
                return driver
            else:
                print("Not found this browser,You can use 'firefox', 'chrome', 'ie' or 'phantomjs'")
        except Exception as msg:
            print("启动浏览器出现异常：%s" % str(msg))

    @threads(n=5)
    def test_run_case(self,name):
        self.driver=self.start(name)
        self.driver.get("http://192.168.17.214/#/")
        time.sleep(3)
        print(self.driver.title)
        self.driver.quit()

if __name__ == "__main__":
    a=Test_method()
    name = ("Chrome", "Firefox")
    for i in name:
        a.test_run_case(i)
        print(111)


    #
    # if __name__=="__main__":
    #     pytest.main(['test_thread.py'])

