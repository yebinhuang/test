import logging
import yaml
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import logging.handlers
from conftest import BASE_DIR


# Android://127.0.0.1:5037/emulator-5554---雷电模拟器
# "Android://127.0.0.1:5037/MDX0220324004291"

class AppDriver:
    config = yaml.safe_load(open(BASE_DIR + '/config/device.yaml', 'r', encoding='utf-8'))['Android']

    @classmethod
    def start(cls):
        logger = logging.getLogger("airtest")
        logger.setLevel(logging.ERROR)
        connect_device("Android://127.0.0.1:5037/{}".format(cls.config['deviceName']))
        start_app(cls.config["appPackage"])
        app_driver = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        time.sleep(1)
        return app_driver

    @classmethod
    def close(cls):
        time.sleep(1)
        stop_app(cls.config["appPackage"])


# 日志配置函数
def logger_config():
    # 1.创建日志器对象
    logger = logging.getLogger()
    # 2.设置日志级别
    logger.setLevel(logging.INFO)
    # 3.创建输出到控制台处理器
    ls = logging.StreamHandler()
    # 4.创建每日生成一个日志文件的处理器
    lht = logging.handlers.TimedRotatingFileHandler(filename=BASE_DIR + "/log/auto_jksjkj_ui.log", when="midnight",
                                                    interval=1,
                                                    backupCount=2)
    # 5.创建格式化器
    formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')
    # 6.处理器绑定格式化器
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)
    # 7.将处理器添加到日志
    logger.addHandler(ls)
    logger.addHandler(lht)
