import allure
import pytest
from time import sleep

from selenium.webdriver.common.by import By

from case.huaxin.data.test_csv import data_csv
from case.huaxin.york.set_app import SetApp
@allure.epic("约克智慧家")
@allure.feature("UI界面测试")
class TestVoice_join:
    # 启动app
    def setup_class(self):
        self.setapp = SetApp()
        self.driver = self.setapp.start_app()
        sleep(1)
        self.setapp.password_login(self.driver, '17853561185', '123456a')
        sleep(1)
      
    # 关闭app
    def teardown_class(self):
        sleep(2)
        self.setapp.stop_app(self.driver)


    # 语音模块
    @allure.description("""  输入语音：打开所有空调（可执行命令） """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("语音模块详细测试1")
    def test_voice1(self,):
        voice_1 = self.setapp.voice_test(self.driver, '打开所有空调',1)

        assert voice_1

    '''

    @allure.description("""  输入语音：打开卧室空调（可执行命令） """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("语音模块详细测试2")
    def test_voice2(self):
        voice_1 = self.setapp.voice_test(self.driver, '打开卧室空调',2)

        assert voice_1

    @allure.description("""  输入语音：开始空调（无效语音命令） """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("语音模块详细测试3")
    def test_voice3(self):
        voice_1 = self.setapp.voice_test(self.driver, '开始空调',3)

        assert voice_1


    @allure.description("""  输入语音：关闭空调（可优化指令） """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("语音模块详细测试4")
    def test_voice4(self):
        voice_1 = self.setapp.voice_test(self.driver, '关闭空调', 4)
        assert voice_1

    '''
    @allure.description("""  使用A账号生成一个新的家庭邀请码，使用B账号进行扫描加入 """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.story("扫码加入家庭")
    def test_login_verification(self):
        aaa = self.setapp.join_home(self.driver)
        assert aaa > 0