# ---------------------- 使用BeautifulReport批量运行测试用例并生成测试报告--------------------------
# 1.导包
import time
import unittest
from BeautifulReport import BeautifulReport

# 文件地址
from ddt import ddt

from conftest import BASE_DIR

suite = unittest.defaultTestLoader.discover(BASE_DIR + '/case', pattern='test*.py')
# 用例名称
description = '健康数据空间公众号项目测试用例'
# 测试报告名称
project_nanme = "健康数据空间项目-测试报告"
file_name = "{}_{}.html".format(project_nanme, time.strftime("%Y-%m-%d-%H-%M-%S"))
# 实例化beautifulReport，filename表示报告文件名称，log_path表示测试报告存放的路径
BeautifulReport(suite).report(filename=file_name, log_path="../report", description=description)
