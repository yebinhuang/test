import logging
import yaml
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


# Android://127.0.0.1:5037/emulator-5554---雷电模拟器
# "Android://127.0.0.1:5037/MDX0220324004291"
class AppDriver:
    config = yaml.safe_load(open('G:/ui_examine/config/device.yaml', 'r', encoding='utf-8'))['Android']

    @classmethod
    def start(cls):
        connect_device("Android://127.0.0.1:5037/{}".format(cls.config['deviceName']))
        start_app(cls.config["appPackage"])
        app_driver = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        time.sleep(1)
        logger = logging.getLogger("airtest")
        logger.setLevel(logging.ERROR)
        return app_driver

    @classmethod
    def quit(cls):
        time.sleep(1)
        stop_app(cls.config["appPackage"])
