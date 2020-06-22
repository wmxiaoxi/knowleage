import pytest
import allure
import sys
@pytest.mark.repeat(2)
@pytest.mark.flaky(reruns=2, reruns_delay=4)
@pytest.mark.run(order=1)
@allure.epic('计算方法为函数，求和')
@allure.feature("测试模块")
@allure.story("用户故事：1")
@allure.title("用例的标题")
@allure.severity("critical")
@pytest.mark.xfail
@pytest.mark.chrome
pytest.main(['-m=chrome','--reruns','2','--reruns-delay','2','--html=report.html'])
@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.skipif(sys.platform == 'win32',reason="does not run on windows")
@pytest.mark.parametrize('qjvalue11,qjvalue12,value13', [(1000, 0, 5)])