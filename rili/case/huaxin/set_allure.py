import time
from datetime import datetime
import json
import os
import shutil
import smtplib
import zipfile
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def set_windos_title(new_title):
    """  设置打开的 Allure 报告的浏览器窗口标题文案
    @param new_title:  需要更改的标题文案 【 原文案为：Allure Report 】
    @return: 没有返回内容，调用此方法传入需要更改的文案即可修改窗体标题文案
    """
    # report_title_filepath：这里主要是去拿到你的HTML测试报告的绝对路径【记得换成你自己的】
    report_title_filepath = r"report\html\index.html"
    # 定义为只读模型，并定义名称为: f
    with open(report_title_filepath, 'r+',encoding="utf-8") as f:
        # 读取当前文件的所有内容
        all_the_lines = f.readlines()
        f.seek(0)
        f.truncate()
        # 循环遍历每一行的内容，将 "Allure Report" 全部替换为 → new_title(新文案)
        for line in all_the_lines:
            f.write(line.replace("Allure Report", new_title))
        # 关闭文件
        f.close()


# 获取 summary.json 文件的数据内容
def get_json_data(name,title_filepath):
    # 定义为只读模型，并定义名称为f
    with open(title_filepath, 'rb') as f:
        # 加载json文件中的内容给params
        params = json.load(f)
        # 修改内容
        params['reportName'] = name
        # 将修改后的内容保存在dict中
        dict = params
    # 关闭json读模式
    f.close()
    # 返回dict字典内容
    return dict


# 写入json文件
def write_json_data(dict,title_filepath):
    # 定义为写模式，名称定义为r
    with open(title_filepath, 'w', encoding="utf-8") as r:
        # 将dict写入名称为r的文件中
        json.dump(dict, r, ensure_ascii=False, indent=4)
    # 关闭json写模式
    r.close()
def wirte_trend():
    file_path = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__))),
                             'report\html\widgets\history-trend.json')
    old_file_path = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__))), 'york\\trend.json')
    # 取出本次执行后的结果
    with open(file_path, "r+") as fp1:
        data1 = json.load(fp1)
    # fp1.truncate(0)
    # 将本次执行的结果添加到历史结果中
    with open(old_file_path, "r") as fp:
        data = json.load(fp)
    # fp.truncate(0)
    # 将新的数据追加到旧的数据中
    data.append(data1[0])
    # 将合并后的数据写入到新json和旧json中
    fh = open(file_path, mode='w')
    fh.write(str(data).replace('\'', '\"'))
    fh2 = open(old_file_path, mode='w')
    fh2.write(str(data).replace('\'', '\"'))

# 压缩文件并发送



def doing():
    title_filepath = r"report\html\widgets\summary.json"
    now_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    set_windos_title("自动化测试报告" + now_time)
    write_json_data(get_json_data("自动化测试报告", title_filepath), title_filepath)
    wirte_trend()
    #yswjfs()

def yswjfs():

    BASE_PATH = os.path.dirname(os.path.realpath(__file__))
    old_path=os.path.join(BASE_PATH, "report")
    yasuobao=os.path.join(BASE_PATH, "report.zip")
    FILE_PATH = os.path.join(BASE_PATH, "mail_report")
    tow_path=os.path.join(BASE_PATH, "mail_report")
    final_path=os.path.join(BASE_PATH, "finalreport.zip")
    #创建一个空文件
    if not os.path.exists(FILE_PATH):
        os.mkdir(FILE_PATH)
    else:
        shutil.rmtree(FILE_PATH)
        os.mkdir(FILE_PATH)
    # 对报告文件夹进行压缩
    with zipfile.ZipFile('report.zip', "w", zipfile.ZIP_DEFLATED) as zf:
        for path, dirnames, filenames in os.walk(old_path):
            fpath = path.replace(old_path, '\\report')
            for filename in filenames:
                zf.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zf.close()
    shutil.move(yasuobao, FILE_PATH)
    shutil.copy('说明.docx', FILE_PATH)
    shutil.copy('generateAllureReport.bat', FILE_PATH)   
    

    # 复制文件后在将整个要发送的文件夹进行压缩

    with zipfile.ZipFile('finalreport.zip', "w", zipfile.ZIP_DEFLATED) as zf:
        for path, dirnames, filenames in os.walk(tow_path):
            fpath = path.replace(tow_path, '\\mail_report')
            for filename in filenames:
                zf.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zf.close()


    # 发送报告

    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    send_usr = 'dgj159415@163.com'  # 发件人
    send_pwd = 'BCLLVAOISZZYGEWK'  # 授权码，邮箱设置
    reverse = '1965265561@qq.com'  # 接收者
    # content1 内容设置
    # content1 = "请查收附件报告，本次自动化测试的执行时间为"+now.strftime("%Y-%m-%d %H:%M:%S")+"，打开附件后有说明文件，按步骤执行即可打开网页版 测试报告，如有问题请及时联系，系统邮件请勿回复。信华信"
    content1 = """

           <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8">
        <title>约克项目-第6次构建</title>
    </head>

    <body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4" offset="0">
        <div width="95%" cellpadding="0" cellspacing="0" style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">
            <div>本邮件由系统自动发出，无需回复！
                <br>
                <br>各位同事，大家好，以下为约克项目自动化测试项目构建信息
                <br>
                <div><font color="#CC0000">构建结果 - 成功！</font></div>
            </div>
            <div>
                <h4><font color="#0B610B">构建信息</font></h4> 
    			<hr size="2" width="100%" />
    			<ul>
    				<li>项目名称 ： 约克智慧家_Android_York_1.1.80.220905143229_alpha.apk</li>
    				<li>构建编号 ： 第6次构建</li>
    				<li>触发原因： 自动触发</li>
    				<li>构建状态： 成功</li>
    				<li>构建日志： <a href="#console">点击查看</a>
    				</li>
    				<li>构建 Url ： <a href="#">点击查看</a>
    				</li>
    				<li>项目 Url ： <a href="#">点击查看</a>
    				</li>
                </ul>
            </div>
            <div>
    			<h4><font color="#0B610B">测试结果</font></h4>
    			<hr size="2" width="100%" />
    			<div>
    			本次测试共执行<b>9</b>个用例，成功<b style="color: green">15</b>个，失败<b style="color: red">0</b>个，跳过<b style="color: #FFEB3B">0</b>个。
    			</div>
    		</div>
            <div>
    			<h4><font color="#0B610B">测试报告</font></h4>
                <hr size="2" width="100%" />
    			<b>点击查看测试报告： <a href="#">查看附件。</a></b>
    		</div>
            <div>
                <h4><font color="#0B610B">失败用例</font></h4>
                <hr size="2" width="100%" />
    			<pre style="font-weight: normal">无
    			</pre>
            </div>
        </div>
    </body>
    </html>

            """
    email_server = 'smtp.163.com'
    email_title = '自动化测试报告' + now.strftime('%Y-%m-%d')
    # -------------
    msg = MIMEMultipart()  # 构建主体
    msg['Subject'] = Header(email_title, 'utf-8')  # 邮件主题
    msg['From'] = send_usr  # 发件人
    msg['To'] = Header('尊敬的各位领导', 'utf-8')  # 收件人--这里是昵称
    msg.attach(MIMEText(content1, 'html', 'utf-8'))  # 构建邮件正文,不能多次构造
    att2 = MIMEText(open('finalreport.zip', 'rb').read(), 'base64', 'utf-8')
    att2['Content-Type'] = 'application/octet-stream'
    att2['Content-Disposition'] = 'attachment;filename="finalreport.zip"'
    msg.attach(att2)

    try:
        smtp = smtplib.SMTP_SSL(email_server)  # 指定邮箱服务器
        smtp.ehlo(email_server)  # 部分邮箱需要
        smtp.login(send_usr, send_pwd)  # 登录邮箱
        smtp.sendmail(send_usr, reverse, msg.as_string())  # 分别是发件人、收件人、格式
        smtp.quit()  # 结束服务
        print('邮件发送完成--')
    except:
        print('发送失败')
    os.remove(final_path)
# if __name__ == '__main__':
#     yswjfs()




