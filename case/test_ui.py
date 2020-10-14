# -*- coding: utf-8 -*-
import logging
import time
import unittest

from BeautifulReport import BeautifulReport
from dateutil.parser import parse
from parameterized import parameterized
from app_util import AppDriver, logger_config
from page.wechat.back_home_page import BackHomePage
from read_data.read_yaml import build_ui_data


class Test(unittest.TestCase):
    # 所有用例后结束
    @classmethod
    def tearDownClass(cls) -> None:
        AppDriver.quit()

    # 启动函数，每个用例测试前，都会执行该函数
    def setUp(self):
        self.start_time = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("开始测试时间：", self.start_time)
        time.sleep(3)

    # 结束函数，每个用例测试结束后，都会执行该函数
    def tearDown(self):
        self.endtime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("测试结束时间：", self.endtime)
        total_time = (self.endtime - self.start_time).total_seconds()
        print("总时长：", total_time, "秒")

    """步骤"""

    # 测试用例1：必须以test_开头
    def test_01(self):
        u"""你好"""
        logging.info("----hhhh---")
        BackHomePage().back_home_page()
        # TencentPage().clear_chat_logs_page(yue_xin_yun)
        # TencentPage().clear_chat_logs_page(jksjkj)
        # JUIPage().jksjkj_ui_page()

    # 读取的数据来源
    data = "ui_examine_data.yaml"
    """数据驱动"""

    @parameterized.expand(build_ui_data())
    def test_02(self, tencent):
        u"""测试用例2"""
        # TencentFindPage().tencent_find_page(tencent)


if __name__ == '__main__':
    unittest.main()
