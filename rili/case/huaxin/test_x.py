import allure
import pytest
from time import sleep

from selenium.webdriver.common.by import By

from case.huaxin.data.test_csv import data_csv
from case.huaxin.york.set_app import SetApp


@allure.epic("约克智慧家")
@allure.feature("关于约克智慧家界面测试")
class TestXY:
    # 启动app
    def setup_class(self):
        self.setapp = SetApp()
        self.driver = self.setapp.start_app()
        sleep(1)
        self.setapp.get_password_login(self.driver, '17853561185', '123456a')
        self.aaa = self.setapp.about(self.driver)

    # 关闭app
    def teardown_class(self):
        sleep(2)
        self.setapp.stop_app(self.driver)


    # 关于约克智慧家界面
    @allure.description("""  测试关于约克智慧家界面是否正常显示 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("关于约克智慧家界面")
    def test_about_york_home(self):
        assert self.aaa[0] > 0.95



    @allure.description("""  测试软件使用条款界面是否正常显示 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("软件使用条款界面")
    def test_software_terms_use(self):
        assert self.aaa[1] > 0.95



    @allure.description("""  测试注销账号界面是否正常显示 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("注销账号界面")
    def test_logout_account(self):
        assert self.aaa[2] > 0.95





