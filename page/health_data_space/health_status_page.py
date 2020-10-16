# -*- coding: utf-8 -*-
import time
from base.base import Base
from page import *
from BeautifulReport import BeautifulReport


class HealthStatusPage(Base):
    # 公共变量----元素
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    def health_status_page(self):
        # 点击健康态势入口
        self.click_5(jkts_rukou)
        # 健康态势断言
        time.sleep(1)
        self.assert_png("健康态势页面", jkts_duanyan)


if __name__ == '__main__':
    HealthStatusPage().health_status_page()
