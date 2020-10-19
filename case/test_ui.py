# -*- coding: utf-8 -*-
import time
import unittest
from dateutil.parser import parse
from app_util import AppDriver
from page.health_data_space.health_record_page import HealthRecordPage
from page.health_data_space.healthy_page import HealthyPage
from page.health_data_space.into_health_record_page import IntoHealthRecordPage
from page.health_data_space.personal_center_page import PersonalCenterPage
from page.wechat.send_a_message_to_me import SendAMessageToMe
from page.wechat.wechat_homepage_assert import BackHomePage
from read_data.read_yaml import build_ui_data
from parameterized import parameterized

"""备注"""
# 读取的数据来源
data = "ui_examine_data.yaml"


# 已认证的情况下
# 小叶  440982202004294294   18866674203

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        AppDriver.start()

    # 所有用例后结束
    @classmethod
    def tearDownClass(cls):
        BackHomePage().back_home_page()
        SendAMessageToMe().send_a_message_to_me("四叶草", "自动化脚本执行完成")
        time.sleep(5)
        AppDriver.close()

    # 启动函数，每个用例测试前，都会执行该函数
    def setUp(self):
        self.start_time = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("开始测试时间：", self.start_time)

    # 结束函数，每个用例测试结束后，都会执行该函数
    def tearDown(self):
        self.endtime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("测试结束时间：", self.endtime)
        total_time = (self.endtime - self.start_time).total_seconds()
        print("总时长：", total_time, "秒")

    """测试用例"""

    # @parameterized.expand(build_ui_data())  # ------>数据驱动<------
    def test_01(self):
        u"""判断是否能进入个人中心页面"""
        PersonalCenterPage().personal_center_page("粤信云")

    def test_02(self):
        u"""判断是否能进入健康态势页面"""
        BackHomePage().back_home_page()
        PersonalCenterPage().personal_center_page("粤信云")
        HealthyPage().healthy_page()

    def test_03(self):
        u"""判断是否能进入2020年10月18日门(急)诊健康档案"""
        BackHomePage().back_home_page()
        PersonalCenterPage().personal_center_page("粤信云")
        HealthyPage().healthy_page()
        HealthRecordPage().health_record_page()

    def test_04(self):
        u"""进入健康档案---病历概要、检查报告(胶片)、一般护理和转院记录"""
        BackHomePage().back_home_page()
        PersonalCenterPage().personal_center_page("粤信云")
        HealthyPage().healthy_page()
        HealthRecordPage().health_record_page()
        IntoHealthRecordPage().into_health_record_page()


if __name__ == '__main__':
    unittest.main()
