import allure
import pytest
from time import sleep

from case.huaxin.data.test_csv import data_csv
from case.huaxin.york.set_app import SetApp

@allure.epic("约克智慧家")
@allure.feature("服务测试页面")
class Testserver:
    def setup_class(self):
        self.setapp = SetApp()
        self.driver = self.setapp.start_app()
        sleep(1)
        self.setapp.get_password_login(self.driver, '17853561185', '123456a')
        self.aaa = self.setapp.service(self.driver)
        self.bbb = self.setapp.fault_query(self.driver)

    # 关闭app
    def teardown_class(self):
        sleep(2)
        self.setapp.stop_app(self.driver)
    # 关于约克智慧家界面


    @allure.description("""  测试服务-热线电话页面是否正常显示 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("热线电话页面")
    def test_tel(self):
        assert self.aaa[0] > 0.95

    @allure.description("""  测试服务-服务政策是否正常显示 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("服务政策页面")
    def test_service(self):
        assert self.aaa[1] > 0.95

    @allure.description("""  测试服务-保养收费页面是否正常显示 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("保养收费页面")
    def test_maintain(self):
        assert self.aaa[2] > 0.95

    @allure.description("""  测试服务-保外费用页面是否正常显示 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("保外费用页面")
    def test_surrender(self):
        assert self.aaa[3] > 0.95

    @allure.description("""  测试故障查询-常见问题页面是否正常显示 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("常见问题页面")
    def test_fault(self):
        assert self.bbb[0] > 0.95

    @allure.description("""  测试故障查询-故障代码页面是否正常显示 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("故障代码")
    def test_03(self):
        assert self.bbb[1] > 0.95

    @allure.description("""  测试是否能够正常提交意见反馈 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("意见反馈")
    def test_yijian(self):
        assert self.bbb[2] > 0.95