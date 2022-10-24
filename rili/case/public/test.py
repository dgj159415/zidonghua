'''
用于测试各种方法的文件

'''
# coding:utf-8
import random
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
import zipfile

import time
import selenium
from appium import webdriver
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 读取txt，将每一行的数据输出
import logger



def zipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    with zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED) as zf:
        for path, dirnames, filenames in os.walk(dirpath):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(dirpath, '')
            for filename in filenames:
                zf.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zf.close()
    print("文件夹\"{0}\"已压缩为\"{1}\".".format(dirpath, outFullName))
# selenium 打开测试
def do_zip_compress(dirpath):
    print("原始文件夹路径：" + dirpath)
    output_name = "{dirpath}.zip"
    parent_name = os.path.dirname(dirpath)
    print("压缩文件夹目录：", parent_name)
    zip = zipfile.ZipFile(output_name, "w", zipfile.ZIP_DEFLATED)
    # 多层级压缩
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            if str(file).startswith("~$"):
                continue
            filepath = os.path.join(root, file)
            print("压缩文件路径：" + filepath)
            writepath = os.path.relpath(filepath, parent_name)
            zip.write(filepath, writepath)
    zip.close()


# def test02():
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     # chrome_options.add_argument("--window-size=1920,1080")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get('http://www.downcc.com/')
#     driver.maximize_window()
#     mima = WebDriverWait(driver, 5, 1).until(EC.presence_of_element_located((By.CLASS_NAME, 'header-searchbtn')))
#     mima.click()
#     # driver.find_element_by_class_name('header-searchbtn').click()
#     # driver.find_element(by=By.CLASS_NAME,value='header-searchbtn').click()
#     sleep(3)
#     driver.quit()
# 测试日志调用组件

def test03():
    logger1 = logger.Logger().logger
    logger1.info("777")
    logger1.critical("dsauhdu")
# 随机数

def test04(long):


    img_name=''
    for i in range(long):
        if i<5:
            tmp=chr(random.randint(65,90))
        else:
            tmp=random.randint(0,9)
        img_name+=str(tmp)
    return img_name

# 启动app
def start_app():
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = '127.0.0.1:62001'
    desired_caps['appPackage'] = 'com.hisensehitachi.iyes2'
    desired_caps['appActivity'] = '.MainActivity'
    desired_caps['automationName'] = 'UiAutomator2'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


# 关闭app
def stop_app(driver):
    driver.terminate_app('com.hisensehitachi.iyes2')
    driver.quit()
def test009():
    return 1,2,3






if __name__ == '__main__':
    aaa=5>4
    print(aaa)

'''
    message = MIMEMultipart('mixed')
    message['From'] = "<dgj159415@163.com>"
    message['To'] = "<1965265561@qq.com>"
    content = MIMEText('******这是zip文件，如果您要下载，请点击******', 'plain', 'utf-8')
    # message['Subject'] = '什么是我的快乐星球'
    message.attach(content)
    message = MIMEMultipart()
    # att2 = MIMEText(open('v1.0.zip', 'rb').read(), 'base64', 'utf-8')
    # att2['Content-Type'] = 'application/octet-stream'
    # att2['Content-Disposition'] = 'attachment;filename="v1.0.zip"'
    # message.attach(att2)
    sender = 'dgj159415@163.com'
    user = 'dgj159415@163.com'
    password = 'BCLLVAOISZZYGEWK'
    smtpserver = 'smtp.163.com'
    receiver = ['1965265561@qq.com']  # receiver 可以是一个list
    smtp = smtplib.SMTP()  # 实例化SMTP对象
    smtp.connect(smtpserver, 25)  # 默认端口是25 也可以根据服务器进行设定
    smtp.login(user, password)  # 登陆smtp服务器
    smtp.sendmail(sender, receiver, message.as_string())  # 发送邮件 ，这里有三个参数
    smtp.quit()

'''

