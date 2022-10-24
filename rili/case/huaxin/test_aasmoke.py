
import allure
import pytest
from time import sleep
from rili.case.huaxin.york.set_app import SetApp
@allure.epic("日立智家")
@allure.feature("冒烟测试")
class TestSmoke:
    # 启动app
    def setup_class(self):
        self.setapp = SetApp()
        self.driver = self.setapp.start_app()
        sleep(2)


    # 关闭app
    def teardown_class(self):
        sleep(2)
        self.setapp.stop_app(self.driver)


    # 密码登录
    @allure.description("""  测试步骤一：使用密码登录，进入首页，判断是否成功登录 """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.story("密码登录")
    def test_login_verification(self):
        login_name = self.setapp.get_password_login(self.driver, '17853552978', '123456a')
        assert login_name != None

    '''
    # 添加家庭
    @allure.description("""  测试步骤二：从首页点击进入家庭页，执行添加家庭操作，判断家庭的总数是否增加 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story('添加家庭')
    @pytest.mark.repeat(1)
    def test_add_home(self):
        a = self.setapp.add_home(self.driver)
        print('-------------------')
        print(a)
        print('-------------------')

        assert a > 0

    
    
    # 删除家庭
    @allure.description("""  测试步骤三：从首页点击进入家庭页，执行删除家庭操作，判断家庭的总数是否减少 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("删除家庭")
    @pytest.mark.repeat(1)
    def test_delete_home(self):
        a = self.setapp.delete_home(self.driver)
        assert a > 0


    # 地址改变
    @allure.description("""  测试步骤四：随机点击地图上的某一点，获取地址栏的文本内容，并和之前的进行比较，若两者不同，则表示用例通过 """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("地址更改")
    # @pytest.mark.flaky(rerun=1)
    # @pytest.mark.repeat(1)
    def test_dress_change(self):
        approximation = self.setapp.dress_change(self.driver)
        assert not approximation

    '''

    @allure.description("""  测试步骤二：语音模块测试，是否正确反应 """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.story("语音测试")
    def test_voice(self):
        len = self.setapp.voice_test(self.driver)
        assert len > 1
        
    # 地图改变
    @allure.description("""  测试步骤三：随机调整地址栏的省市区，截图调整后的地图，并和之前的进行比较，若两者相似度小于0.86，则表示测试通过 """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("地图更改")
    # @pytest.mark.repeat(3)
    def test_map_change(self):
        approximation = self.setapp.map_selection(self.driver)
        assert approximation < 0.86

    @pytest.mark.flaky(reruns=1, reruns_delay=2)
    @allure.description("""  随机更换系统相册中的头像，第1次更换 """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("更换头像1")
    def test_replace_picture2(self):
        approximation = self.setapp.change_head_portrait(self.driver)
        assert approximation < 0.81
    
    # 退出登录
    @allure.description("""  测试步骤六：退出登录，判断是否成功退出 """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("退出登录")
    # @pytest.mark.repeat(3)
    def test_exit_login(self):
        exit_login = self.setapp.exit_login(self.driver)
        assert exit_login == '登录'
    
    # 是否记住密码
    @allure.description("""  测试步骤七：是否记住密码，判断退出登录后，密码框是否存在密码 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("记住密码")
    def test_remember_password(self):
        password = self.setapp.remember_password(self.driver)
        assert len(password) > 0
        #assert True


    '''
    # 验证码登录
    @allure.description("""  测试步骤八：使用验证码登录，进入首页，判断是否成功登录 """)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("验证码登录")
    def test_verification_code_login(self):
        login_name = self.setapp.verification_code_login(self.driver)
        assert login_name != None
    '''
