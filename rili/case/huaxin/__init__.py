import os

import pytest



if __name__ == "__main__":
     pytest.main(['-s'])
    #test11()
    # url = 'https://hitachi-iez-bucket.oss-cn-hangzhou.aliyuncs.com/York_1.1.80.220905143229_alpha.apk?Expires=1977719665&OSSAccessKeyId=LTAIDueQ1ezjjiBQ&Signature=eEOFz71WmZNeoBznSDz8SOxyDbg%3D'
    # r = requests.get(url=url)
    # BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # FILE_PATH = os.path.join(BASE_PATH, "apk")
    # final_file_path = os.path.join(FILE_PATH, '约克智慧家.apk')
    # with open(final_file_path, 'wb') as output:
    #     output.write(r.content)
    # os.system("adb uninstall com.hisensehitachi.iyes2")
    # os.system("adb install " + final_file_path)
    #

    # pytest.main(['--alluredir', 'report/result'])
    # split = 'allure ' + 'generate ' + './report/result ' + '-o ' + './report/html ' + './report --clean'
    # os.system(split)
    # doing()



