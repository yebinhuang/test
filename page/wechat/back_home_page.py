# 退出H5页面回到微信主页
# -*- coding: utf-8 -*-
from base.base import Base
from page import *
from BeautifulReport import BeautifulReport


class BackHomePage(Base):
    # 公共变量----元素
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    def back_home_page(self, num=1):
        # self.p_click(quit_h5_btn)
        # # 调用退出H5
        # for i in range(num):
        #     self.back_btn()
        self.assert_png("主页", zhuye)


if __name__ == '__main__':
    BackHomePage().back_home_page()
