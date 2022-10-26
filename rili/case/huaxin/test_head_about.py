import allure
import pytest
from time import sleep
from case.huaxin.york.set_app import SetApp


@allure.epic("约克智慧家")
@allure.feature("头像模块/关于约克智慧家模块测试")
class TestHead_about:
    # 启动app
    def setup_class(self):
        self.setapp = SetApp()
        self.driver = self.setapp.start_app()
        sleep(1)
        self.setapp.password_login(self.driver, '17853561185', '123456a')
        self.approximation = self.setapp.change_head_portrait(self.driver)
    # 关闭app
    def teardown_class(self):
        sleep(2)
        self.setapp.stop_app(self.driver)



    # 更换头像
    @allure.description("""  随机更换系统相册中的头像，第一次更换 """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("更换头像1")
    def test_replace_picture1(self):
        assert self.approximation[0] < 0.81

    # @allure.description("""  随机更换系统相册中的头像，第二次更换 """)
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.story("更换头像2")
    # def test_replace_picture2(self):
    #
    #     assert approximation < 0.81
    #
    # @allure.description("""  随机更换系统相册中的头像，第三次更换 """)
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.story("更换头像3")
    # def test_replace_picture3(self):
    #     assert approximation < 0.81


    # 关于约克智慧家界面
    @allure.description("""  测试关于约克智慧家界面是否正常显示 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("关于约克智慧家界面")
    def test_about_york_home(self):
        assert self.approximation[1] > 0.95

    @allure.description("""  测试软件使用条款界面是否正常显示 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("软件使用条款界面")
    def test_software_terms_use(self):
        assert self.approximation[2] > 0.95

    @allure.description("""  测试注销账号界面是否正常显示 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("注销账号界面")
    def test_logout_account(self):
        assert self.approximation[3] > 0.95

