'''
封装日志打印模块，调用时导入包，实例化对象：
    logger1 = logger.Logger().logger
调用示例：
    logger1.info("---测试---")
关于日志级别：
    DEBUG：详细的信息,通常只出现在诊断问题上
    INFO：确认一切按预期运行
    WARNING：一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。
    ERROR：更严重的问题,软件没能执行一些功能
    CRITICAL：一个严重的错误,这表明程序本身可能无法继续运行
'''

import logging, time, os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger():
    def __init__(self):
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)
        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

# 本地化测试日志打印
#logger = Logger().logger
# if __name__ == '__main__':
#     logger.info("---测试什么时候---")
#     logger.debug("---测试现在打打打---")
