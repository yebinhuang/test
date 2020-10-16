# -*- coding: utf-8 -*-
import logging
import time
import unittest
from dateutil.parser import parse
from parameterized import parameterized
from app_util import AppDriver
from page.health_data_space.health_record_page import HealthRecordPage
from page.health_data_space.personal_center_page import PersonalCenterPage
from page.wechat.wechat_homepage_assert import BackHomePage
from read_data.read_yaml import build_ui_data

"""备注"""
# 读取的数据来源
data = "ui_examine_data.yaml"


# 已认证的情况下
# 小叶  440982202004294294   18866674203

class Test(unittest.TestCase):
    # 所有用例后结束
    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        AppDriver.close()

    # 启动函数，每个用例测试前，都会执行该函数
    def setUp(self):
        self.start_time = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("开始测试时间：", self.start_time)

    # 结束函数，每个用例测试结束后，都会执行该函数
    def tearDown(self):
        time.sleep(1)
        BackHomePage().back_home_page()
        self.endtime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("测试结束时间：", self.endtime)
        total_time = (self.endtime - self.start_time).total_seconds()
        print("总时长：", total_time, "秒")

    """测试用例"""

    @parameterized.expand(build_ui_data())  # ------>数据驱动<------
    def test_01(self, tencent):
        u"""判断是否能进入主页页面"""
        PersonalCenterPage().personal_center_page(tencent)

    def test_02(self):
        u"""判断是否能进入健康态势页面"""
        PersonalCenterPage().personal_center_page("粤信云")
        HealthRecordPage().health_record_page()

    def test_03(self):
        u"""判断是否能进入对应的健康档案"""
        PersonalCenterPage().personal_center_page("粤信云")
        HealthRecordPage().health_record_page()



if __name__ == '__main__':
    unittest.main()
