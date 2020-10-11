# 1.导包
import time
import unittest

from BeautifulReport import BeautifulReport
# from lib.HTMLTestRunner import HTMLTestRunner
# from lib.HTMLTestRunnerCN import HTMLTestRunnerCN

# 2.组织测试套件  # unittest.TestSuite()


suite = unittest.TestLoader().discover("G:/ui_examine/case", pattern="test*")


# ---------------------- 方法一：使用测试运行器批量运行测试用例不生成测试报告-----------------------
# # 3.实例化运行器对象
# runner = unittest.TextTestRunner()
#
# # 4.运行测试用例
# runner.run(suite)

# 3.定义测试报告文件路径 (方法二和方法三需要定义测试报告路径)
# report_path = "../report/report_{}.html".format(time.strftime("%Y%m%d%H%M%S"))

# ---------------------- 方法二：使用HTMLTestRunner批量运行测试用例并生成测试报告-----------------------
# with open(report_path, 'wb') as f:
#     # 5.实例化HTMLTestRunner对象
#     runner = HTMLTestRunner(f, title="test_report", description="CHROME")
#
#     # 6.运行测试套件
#     runner.run(suite)


# # ---------------------- 方法三：使用HTMLTestRunnerCN批量运行测试用例并生成测试报告-----------------------
# with open(report_path, 'wb') as f:
#     # 5.实例化HTMLTestRunner对象
#     runner = HTMLTestRunnerCN.HTMLTestReportCN(f, title="test_report", description="CHROME")
#
#     # 6.运行测试套件
#     runner.run(suite)
#
#
# # 关闭浏览器关闭开关
# DriverUtils.open_key(False)


# # ---------------------- 方法四：使用BeautifulReport批量运行测试用例并生成测试报告--------------------------
# # 定义测试报告名称
file_name = "report_{}.html".format(time.strftime("%Y%m%d%H%M%S"))
#
# 实例化beautifulReport，filename表示报告文件名称，log_path表示测试报告存放的路径
BeautifulReport(suite).report(filename=file_name, log_path="../report", description="CHROME")


