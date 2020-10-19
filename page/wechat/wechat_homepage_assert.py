# 退出H5页面回到微信主页
# -*- coding: utf-8 -*-
import time
from dateutil.parser import parse
from app_util import AppDriver
from base.base import Base
from page import *


class BackHomePage(Base):
    # 公共变量----元素
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    # 统一用2次返回，退回微信主页的判断
    def back_home_page(self, num=2):
        # 加入主页判断
        self.p_click(quit_h5_btn)
        # 调用退出H5
        for i in range(num):
            self.back_btn()
        else:
            pass
        # 不成功的执行
        time.sleep(1)
        homepage = self.assert_png("微信主页断言-", zhuye)
        i = "微信主页"
        if i in homepage:
            AppDriver().close()
            AppDriver().start()
            time.sleep(6)
            self.assert_png("关闭微信APP后的主页页面-", zhuye)


if __name__ == '__main__':
    BackHomePage().back_home_page()
