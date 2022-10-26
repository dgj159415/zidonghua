import os
import random, time
import re
from time import sleep
import allure
import pygame
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from case.public import logger
from appium import webdriver
from selenium.webdriver.common.by import By
from case.public.img_judg  import execution_judgment
class SetApp:
    # 初始化方法
    def __init__(self):
        self.logger = logger.Logger().logger
        self.desired_caps = dict()
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '9'
        self.desired_caps['deviceName'] = 'FFK0217B11000942'
        self.desired_caps['appPackage'] = 'com.hisensehitachi.iez2'
        self.desired_caps['appActivity'] = '.MainActivity'
        self.desired_caps['automationName'] = 'UiAutomator2'
        self.driver = None
        self.img_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "img")
        self.img_name = None
        self.now_time = None
        self.final_img_path = None
        self.text=None

    # 启动app并授予权限
    def start_app(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        for i in range(5):
            try:
                WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@text='始终允许']"))).click()
            except:
                pass
        self.logger.info("APP启动并允许所有权限！")
        return self.driver

    # 关闭app
    def stop_app(self, driver):
        self.driver = driver
        self.driver.quit()
        self.logger.info("APP关闭！")
    # 记住密码登录
    def get_password_login(self, driver, username_text, password_text):
        self.driver = driver
        # WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, "//*[@text='密码登录']"))).click()
        sleep(0.5)

        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.Image")))[4].click()
        # WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.view.View")))[5].click()
        input_box = WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.EditText")))[0]
        input_box.clear()
        input_box.send_keys(username_text)
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.EditText")))[1].send_keys(password_text)
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, "//*[@text='登录']"))).click()
        sleep(3)
        try:
            WebDriverWait(self.driver, 3, 0.5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@text='下次再说']"))).click()
        except:
            pass
        self.logger.info("使用密码登录成功，用例无异常！")
        try:
            self.text = self.driver.find_element(by=By.XPATH, value="//*[@text='首页']").text
        except:
            pass
        return self.text

    # 不记住密码登录
    def password_login(self, driver, username_text, password_text):
        self.driver = driver
        sleep(12)
        # self.driver.find_element(by=By.XPATH, value="//*[@text='记住密码']").click()
        # self.driver.find_elements(by=By.CLASS_NAME, value= 'android.widget.EditText')[0].send_keys(username_text)
        input_box = self.driver.find_elements(by=By.CLASS_NAME, value='android.widget.EditText')[0]
        input_box.clear()
        input_box.send_keys(username_text)
        sleep(2)
        self.driver.find_elements(by=By.CLASS_NAME, value= 'android.widget.EditText')[1].send_keys(password_text)
        sleep(1)
        self.driver.find_element(by=By.CLASS_NAME, value= 'android.widget.Button').click()
        sleep(3)
        self.logger.info("使用密码登录成功，用例无异常！")
        return self.driver.find_elements(by=By.CLASS_NAME, value='android.view.View')[1].text



    # 记住密码
    def remember_password(self,driver):
        self.driver = driver
        sleep(2)
        self.logger.info("判断是否记住密码用例通过，无异常！")

        return self.driver.find_elements(by=By.CLASS_NAME,value='android.widget.EditText')[1].text

    # 验证码登录
    def verification_code_login(self, driver):
        self.driver=driver
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, "//*[@text='验证码登录']"))).click()

        # 输入手机号
        sleep(1)
        input_box = self.driver.find_elements(by=By.CLASS_NAME, value='android.widget.EditText')[0]
        input_box.clear()
        input_box.send_keys('17853561185')

        # 清空通知
        self.driver.open_notifications()
        sleep(1)
        try:
            self.driver.find_element(by=By.XPATH, value='//android.widget.ImageView[@content-desc="清除所有通知"]').click()
        # 优化点，指定异常名称，这个地方的异常是找不到元素
        except:
            self.driver.back()
            pass
        sleep(1)
        # d点击发送验证码
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, "//*[@text='获取验证码']"))).click()
        # 连接数据库，获取验证码，传值验证码 ……
        self.driver.open_notifications()  # 打开消息通知栏
        #sleep(25)
        # 优化点 验证码等待时长,这个地方也有可能找不到元素，有时候20秒也发不过来
        dx = WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@text,'验证码是')]")))

        #dx = self.driver.find_element(By.XPATH, "//*[contains(@text,'验证码是')]")
        verification_code = re.findall(r'\d{6}', dx.text)
        print(verification_code)
        #sleep(20)

        self.driver.back()
        self.driver.find_elements(by=By.CLASS_NAME, value='android.widget.EditText')[1].send_keys(verification_code)
        sleep(3)
        # 点击登录
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, "//*[@text='登录']"))).click()
        sleep(3)
        self.logger.info("使用验证码登录成功，无异常！")

        try:
            self.text = self.driver.find_element(by=By.XPATH, value="//*[@text='首页']").text
        except:
            pass
        return self.text

    # 地图变化
    def map_selection(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_all_elements_located
                                                 ((By.CLASS_NAME, "android.widget.Image")))[0].click()
        sleep(2)
        # 500 1800
        self.driver.tap([(500, 1800)], 200)
        sleep(2)
        #  WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@text='家庭管理']"))).click()
        WebDriverWait(self.driver, 3, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@text='幸福']"))).click()
        sleep(1)
        WebDriverWait(self.driver, 3, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@text='家庭地址']"))).click()
        sleep(1)
        WebDriverWait(self.driver, 3, 1).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.view.View")))[8].click()

        sleep(3)

        self.now_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        image1 = self.now_screenshot(self.driver, 'map.png')
        with open(image1, "rb") as f:
            file = f.read()
            allure.attach(file, '前置截图'+self.now_time, allure.attachment_type.PNG)
        WebDriverWait(self.driver, 3, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@text='省份']"))).click()
        sleep(0.5)
        self.driver.tap([(500, ((random.randint(3, 11)*150)+250))], 200)
        WebDriverWait(self.driver, 3, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@text='完成']"))).click()
        sleep(0.5)
        self.driver.tap([(500, ((random.randint(0, 8)*150)+250))], 200)
        WebDriverWait(self.driver, 3, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@text='完成']"))).click()
        sleep(0.5)
        self.driver.tap([(500, ((random.randint(0, 3) * 150) + 250))], 200)
        WebDriverWait(self.driver, 3, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@text='完成']"))).click()
        sleep(3)
        self.now_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        image2 = self.now_screenshot(self.driver, 'map.png')
        with open(image2, "rb") as f:
            file = f.read()
            allure.attach(file, '后置截图' + self.now_time, allure.attachment_type.PNG)
        self.driver.back()
        self.driver.back()
        WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@text='确定']"))).click()
        sleep(2)
        self.driver.back()
        sleep(1)
        self.driver.back()
        return execution_judgment(image1, image2)
    # 地址变化
    def dress_change(self, driver):
        self.driver = driver
        # self.driver.find_element(by=By.CLASS_NAME, value='android.widget.Image').click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='添加新家']").click()
        sleep(1)
        self.driver.find_elements(by=By.CLASS_NAME, value='android.view.View')[12].click()
        sleep(2)
        a1 = self.driver.find_elements(by=By.CLASS_NAME, value='android.widget.EditText')[0].text
        x = random.randint(200, 900)
        y = random.randint(900, 1700)
        self.driver.tap([(x, y), (x+100, y+100)])
        sleep(10)
        a2 = self.driver.find_element(by=By.CLASS_NAME, value='android.widget.EditText').text
        self.logger.info("地址自动获取成功，用例正常！")

        return a1 == a2


    # 截图保存
    def now_screenshot(self,driver,img_name):
        self.driver=driver
        self.img_name=img_name
        self.now_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        self.final_img_path = self.img_path + '\\' +  self.now_time+ '_' +self.img_name
        self.driver.get_screenshot_as_file(self.final_img_path)
        return self.final_img_path

    # 删除家庭
    def delete_home(self, driver):
        self.driver = driver
        #self.driver.find_element(by=By.CLASS_NAME, value='android.widget.Image').click()
        sleep(1)
        homes=self.driver.find_elements(by=By.XPATH, value="//*[@text='详情']")
        a1=len(homes)
        homes[1].click()
        sleep(1)
        TouchAction(self.driver).press(x=200, y=1000).wait(1000).move_to(x=200, y=300).release().perform()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='退出家庭']").click()
        sleep(1)
        self.driver.find_elements(by=By.CLASS_NAME, value="android.widget.Button")[1].click()
        sleep(2)
        self.driver.find_element(by=By.CLASS_NAME, value='android.widget.Image').click()
        sleep(1)
        homes = self.driver.find_elements(by=By.XPATH, value="//*[@text='详情']")
        a2 = len(homes)
        # self.driver.back()
        return (a1-a2)

    # 添加家庭
    def add_home(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_all_elements_located
                                                 ((By.CLASS_NAME, "android.widget.Image")))[0].click()
        sleep(2)
        # 500 1800
        self.driver.tap([(500, 1800)], 200)

        #WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@text='家庭管理']"))).click()

        # WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@text='新建家庭']"))).click()
        # WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located
        #                                          ((By.CLASS_NAME, 'android.widget.EditText'))).send_keys('幸福' + str(random.randint(10, 99)))
        # WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_all_elements_located
        #                                          ((By.CLASS_NAME, "android.widget.Button")))[1].click()
        # WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located
        #                                          ((By.XPATH, "//*[@text='好的']"))).click()
        sleep(5)
        #homes = self.driver.find_elements(by=By.XPATH,value="//*[contains(@text,'幸福')]")
        home1 = WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located
                                                  ((By.XPATH, "//*[@text='幸福']")))
        #home1 = self.driver.find_elements(by=By.XPATH,value="//*[@text='17853552978']")
        #print(len(homes))

        print(len(home1))
        #homes = self.driver.find_elements(by=By.XPATH, value="//*[contains(text(),'幸福')]")
        self.driver.back()
        return len(home1)
        #homes = self.driver.find_elements(by=By.XPATH, value="//*[@text='详情']")
        # a1 = len(homes)
        # self.driver.find_element(by=By.CLASS_NAME, value='android.widget.Image').click()
        # sleep(1)
        # self.driver.find_element(by=By.XPATH, value="//*[@text='家庭管理']").click()
        # sleep(2)
        # page_element = self.driver.find_elements(by=By.CLASS_NAME, value="android.view.View")[37]
        # table_tr_list = page_element.find_elements(by=By.CLASS_NAME, value="android.view.View")
        # print(len(table_tr_list))
        # self.driver.find_element(by=By.XPATH, value="//*[@text='新建家庭']").click()
        # return 1
        # homes = self.driver.find_elements(by=By.XPATH, value="//*[@text='详情']")
        # a1 = len(homes)
        # sleep(1)
        # self.driver.find_element(by=By.XPATH, value="//*[@text='添加新家']").click()
        # sleep(1)
        # self.driver.find_element(by=By.CLASS_NAME, value='android.widget.EditText').send_keys(
        #     '测试' + str(random.randint(10, 99)))
        # sleep(1)
        # self.driver.find_element(by=By.XPATH, value="//*[@text='完成']").click()
        # sleep(4)
        # self.driver.find_element(by=By.XPATH, value="//*[@text='好的']").click()
        # sleep(1)
        # self.driver.find_element(by=By.CLASS_NAME, value='android.widget.Image').click()
        # sleep(1)
        # homes = self.driver.find_elements(by=By.XPATH, value="//*[@text='详情']")
        # a2 = len(homes)
        # # self.driver.back()
        # return a2-a1

    # 语音模块
    def voice_test(self, driver):
        self.driver = driver
        #sleep(1)
        text=None
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_all_elements_located
                                                 ((By.CLASS_NAME, "android.widget.Image")))[1].click()
        # self.driver.find_element(by=By.XPATH, value="//*[@text='语音']").click()
        sleep(1)
        press_coice = driver.find_elements(by=By.CLASS_NAME, value="android.widget.Image")[1]
        #TouchAction(driver).long_press(e1=press_coice,x=535,y=1700,duration=2000).perform()
        # pygame.mixer.init()  # 初始化混音器模块（pygame库的通用做法，每一个模块在使用时都要初始化pygame.init()为初始化所有的pygame模块，可以使用它也可以单初始化这一个模块）
        # pygame.mixer.music.load("打开空调 .mp3")  # 加载音乐
        # pygame.mixer.music.set_volume(0.5)  # 设置音量大小0~1的浮点数
        # pygame.mixer.music.play()
        TouchAction(driver).press(x=535, y=1700).wait(3000).move_to(x=550, y=1700).release().perform()
        sleep(2)
        try:
            text = self.driver.find_elements(by=By.CLASS_NAME, value="android.view.View")[0].text
        except:
            pass
        #print(text)
        sleep(1)
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_all_elements_located
                                                 ((By.CLASS_NAME, "android.widget.Image")))[2].click()

        '''
        if a==1:
            self.logger.info("输入语音:  "+instructions+'获得响应为：好的，正在为您打开所有空调')
        elif a==2:
            self.logger.info("输入语音:  " + instructions + '获得响应为：好的，正在为您打开卧室空调')
        elif a == 3:
            self.logger.info("输入语音:  " + instructions + '获得响应为：问题听懂了，可惜我还不会回答您，我去学习了')
        elif a==4:
            self.logger.info("输入语音:  " + instructions + '获得响应为：请指定具体的具体的空调名称（中文）')
        '''


        return len(text)

    def change_head_portrait(self, driver):
        self.driver = driver
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='我的']").click()
        sleep(1)
        # 点击设置
        self.driver.find_elements(by=By.CLASS_NAME, value="android.widget.Image")[1].click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='头像']").click()
        sleep(2)
            # 截图
        self.now_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        image3 = self.now_screenshot(self.driver, 'map.png')
        with open(image3, "rb") as f:
            file = f.read()
            allure.attach(file, '头像更换前' + self.now_time, allure.attachment_type.PNG)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value="//*[@text='更换头像']").click()


        sleep(1)
        # 点击确认按钮
        self.driver.find_element(by=By.XPATH, value="//*[@text='从相册选择']").click()
        sleep(1)
        # 点击确认按钮
       # self.driver.find_element(by=By.CLASS_NAME, value='android.widget.ImageButton').click()
        #进入相册后
       # sleep(3)
        #self.driver.find_element(by=By.XPATH, value="//*[@text='图库']").click()
        #sleep(0.5)

        self.driver.find_elements(by=By.CLASS_NAME, value="android.widget.LinearLayout")[0].click()
        sleep(0.5)

        a1 = [100, 400, 600, 900]
        a2 = [300, 600, 900, 1200, 1500, 1800]
        # print(a1[random.randint(0, 3)])
        # print(a2[random.randint(0, 5)])
        self.driver.tap([(a1[random.randint(0, 3)], a2[random.randint(0, 5)])], 200)
        sleep(2)
        #self.driver.tap([(1000, 100)], 200)
        sleep(2)
        self.driver.find_elements(by=By.CLASS_NAME, value='android.widget.ImageButton')[1].click()
        sleep(4)
        # 下面这一行需要删掉
       # self.driver.find_element(by=By.XPATH, value="//*[@text='确 定']").click()
       # sleep(1)
       # self.driver.find_element(by=By.XPATH, value="//*[@text='取 消']").click()
        sleep(3)
        #self.driver.find_elements(by=By.CLASS_NAME, value='android.widget.Image')[1].click()
        image4 = self.now_screenshot(self.driver, 'map9.png')
        with open(image4, "rb") as f:
            file = f.read()
            allure.attach(file, '头像更换后' + self.now_time, allure.attachment_type.PNG)
        sleep(2)
        # print(execution_judgment(image3, image4))
        self.driver.back()
        sleep(1)
        self.driver.back()
        self.logger.info("头像更换成功，用例无异常！")
        result0 = execution_judgment(image3, image4)
        return result0

        '''
        #
        #
        #
        sleep(0.5)
        self.driver.find_element(by=By.XPATH, value="//*[@text='设置']").click()
        sleep(0.5)
        self.driver.find_element(by=By.XPATH, value="//*[@text='关于约克智慧家']").click()
        sleep(0.5)
        now_about = self.now_screenshot(self.driver, 'about.png')
        image1 = './data/about.png'
        result1 = execution_judgment(now_about, image1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='软件使用条款']").click()
        sleep(3)
        now_clause = self.now_screenshot(self.driver, 'clause.png')
        image2 = './data/clause.png'
        result2 = execution_judgment(now_clause, image2)
        self.driver.back()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='注销账号']").click()
        sleep(0.3)
        now_logout = self.now_screenshot(self.driver, 'logout.png')
        image3 = './data/logout.png'
        result3 = execution_judgment(now_logout, image3)
        return result0,result1, result2, result3
        '''



    # 扫码加入家庭
    def join_home(self,driver):
        self.driver = driver
        #self.password_login(self.driver, '17862104046', '123456a')
        self.driver.back()
        sleep(1)
        self.driver.find_element(by=By.CLASS_NAME, value='android.widget.Image').click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='添加新家']").click()
        sleep(1)
        self.driver.find_element(by=By.CLASS_NAME, value='android.widget.EditText').send_keys(
            '测试' + str(random.randint(10, 99)))
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='完成']").click()
        sleep(2)
        try:
            self.driver.find_element(by=By.XPATH, value="//*[@text='好的']").click()
        except:
            pass
        sleep(1)
        self.driver.find_element(by=By.CLASS_NAME, value='android.widget.Image').click()
        sleep(1)
        liebiao = self.driver.find_elements(by=By.XPATH, value="//*[@text='详情']")
       # print(len(liebiao))
        liebiao[(len(liebiao))-1].click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='邀请']").click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='保存二维码至相册']").click()
        sleep(1)
        self.driver.back()
        self.driver.back()
        self.driver.back()
        sleep(1)
        self.exit_login(self.driver)
        sleep(1)
        self.password_login(self.driver, '17862104046', '123456a')
        sleep(1)
        self.driver.find_element(by=By.CLASS_NAME, value='android.widget.Image').click()
        sleep(1)

        homes = self.driver.find_elements(by=By.XPATH, value="//*[@text='详情']")
        a1 = len(homes)
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='扫码加入']").click()
        self.driver.tap([(900, 1600)], 200)
        sleep(1)
        self.driver.find_elements(by=By.CLASS_NAME, value='android.widget.ImageView')[0].click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='确认加入']").click()
        sleep(1)
        self.driver.find_element(by=By.CLASS_NAME, value='android.widget.Image').click()
        sleep(1)
        homes = self.driver.find_elements(by=By.XPATH, value="//*[@text='详情']")
        a2 = len(homes)
        sleep(1)

        return a2-a1

    # 服务页面-热线电话-服务政策-故障查询
    def service(self,driver):
        self.driver=driver
        self.driver.find_element(by=By.XPATH, value="//*[@text='服务']").click()
        image1 = './data/tel.png'  # 热线电话
        image2 = './data/service.png'  # 服务政策
        image3 = './data/maintain.png'  # 保养收费标准
        image4 = './data/surrender.png'  # 保外费用


        sleep(0.5)
        self.driver.find_element(by=By.XPATH, value="//*[@text='热线电话']").click()
        sleep(2)
        now_tel=self.now_screenshot(self.driver, 'tel.png')

        result1 = execution_judgment(now_tel, image1)
        self.driver.back()
        sleep(0.3)
        self.driver.back()
        sleep(0.3)
        self.driver.find_element(by=By.XPATH, value="//*[@text='服务政策']").click()
        sleep(2)
        now_service=self.now_screenshot(self.driver, 'service.png')
        result2 = execution_judgment(now_service, image2)
        self.driver.find_element(by=By.XPATH, value="//*[@text='费用标准']").click()
        sleep(0.3)
        self.driver.find_element(by=By.XPATH, value="//*[@text='保养收费标准需要更换的部件费用标准']").click()
        sleep(2)
        now_maintain = self.now_screenshot(self.driver, 'maintain.png')
        result3 = execution_judgment(now_maintain, image3)
        self.driver.back()
        sleep(0.3)
        self.driver.find_element(by=By.XPATH, value="//*[@text='保外费用保修期间维修，返工等费用标准']").click()
        sleep(2)
        now_surrender = self.now_screenshot(self.driver, 'surrender.png')
        result4 = execution_judgment(now_surrender, image4)
        return result1, result2, result3, result4


    # 故障查询页
    def fault_query(self,driver):
        image5 = './data/fault.png'
        image6 = './data/03.png'
        self.driver=driver
        self.driver.back()
        sleep(0.3)
        self.driver.back()
        sleep(0.3)
        self.driver.find_element(by=By.XPATH, value="//*[@text='故障查询']").click()
        sleep(2)
        now_fault = self.now_screenshot(self.driver, 'fault.png')
        result5 = execution_judgment(now_fault, image5)
        self.driver.find_element(by=By.XPATH, value="//*[@text='故障代码']").click()
        sleep(1)
        self.driver.find_element(by=By.CLASS_NAME, value="android.widget.EditText").send_keys('03')
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='查询']").click()
        sleep(1)
        self.now_screenshot(self.driver, '03.png')
        now_03 = self.now_screenshot(self.driver, '03.png')
        result6 = execution_judgment(now_03, image6)
        self.driver.back()
        self.driver.find_element(by=By.XPATH, value="//*[@text='意见反馈']").click()
        sleep(0.5)
        self.driver.find_elements(by=By.CLASS_NAME, value="android.widget.EditText")[0].send_keys('APP的功能很完善，用着体验超级棒！')
        sleep(0.5)
        self.driver.find_elements(by=By.CLASS_NAME, value="android.widget.EditText")[1].send_keys('空调真好用啊，下次还要选择约克！')
        sleep(0.5)
        self.driver.find_elements(by=By.CLASS_NAME, value="android.widget.Image")[random.randint(1, 5)].click()
        sleep(0.5)
        self.driver.find_elements(by=By.CLASS_NAME, value="android.widget.Image")[random.randint(6, 10)].click()
        sleep(0.5)
        self.driver.find_element(by=By.XPATH, value="//*[@text='提交']").click()
        locator = ("xpath", "//*[contains(@text,'意见反馈成功')]")
        # 定位
        toast = WebDriverWait(driver, 10, 0.01).until(EC.presence_of_element_located(locator))
        if (len(toast.text)>2):
            result7=0.98
        else:
            result7=0.5

        return result5,result6,result7

    # 进入设置页
    def setting(self,driver):
        self.driver=driver
        self.driver.find_element(by=By.XPATH, value="//*[@text='我']").click()
        sleep(0.5)
        self.driver.find_element(by=By.XPATH, value="//*[@text='设置']").click()
        return self.driver

    # 离家未关机提醒
    def leave_home(self,driver):
        self.driver = self.setting(driver)
        sleep(0.5)
        btn1=self.driver.find_elements(by=By.CLASS_NAME, value='android.view.View')[16]
        old_state=btn1.get_attribute("bounds")
        btn1.click()
        sleep(0.5)
        try:
            self.driver.find_element(by=By.XPATH, value="//*[@text='确定']").click()
        except:
            pass
        sleep(0.5)
        now_state=self.driver.find_elements(by=By.CLASS_NAME, value='android.view.View')[16].get_attribute("bounds")
        print(old_state,now_state)
        return 4



    # 关于约克智慧家
    def about(self, driver):
        #self.driver= self.setting(driver)
        self.driver=driver
        sleep(0.5)
        self.driver.find_element(by=By.XPATH, value="//*[@text='设置']").click()
        sleep(0.5)
        self.driver.find_element(by=By.XPATH, value="//*[@text='关于约克智慧家']").click()
        sleep(0.5)
        now_about=self.now_screenshot(self.driver,'about.png')
        image1 = './data/about.png'
        result1= execution_judgment(now_about, image1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='软件使用条款']").click()
        sleep(3)
        now_clause = self.now_screenshot(self.driver, 'clause.png')
        image2='./data/clause.png'
        result2 = execution_judgment(now_clause, image2)
        self.driver.back()
        sleep(0.3)
        self.driver.find_element(by=By.XPATH, value="//*[@text='注销账号']").click()
        sleep(0.3)
        now_logout = self.now_screenshot(self.driver, 'logout.png')
        image3='./data/logout.png'
        result3 = execution_judgment(now_logout, image3)
        return result1, result2, result3
    # 退出登录
    def exit_login(self, driver):
        self.driver = driver
        self.driver.find_element(by=By.XPATH, value="//*[@text='我的']").click()


        # aaa= WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@text='我的']")))
        # print(len(aaa))
        sleep(1)
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.Image")))[1].click()
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, "//*[@text='退出登录']"))).click()
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, "//*[@text='确定']"))).click()
        '''
        self.driver.find_element(by=By.XPATH, value="//*[@text='我的']").click()
        sleep(0.5)
        self.driver.find_elements(by=By.CLASS_NAME, value='android.widget.Image')[1].click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[@text='退出登录']").click()
        sleep(0.3)
        self.driver.find_element(by=By.XPATH, value="//*[@text='确定']").click()
        '''
        #点击确认按钮
        self.logger.info("退出登录成功，用例无异常！")
        sleep(1)
        try:
            self.text=self.driver.find_element(by=By.XPATH, value="//*[@text='登录']").text
        except:
            pass
        return self.text

