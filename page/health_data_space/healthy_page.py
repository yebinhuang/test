# -*- coding: utf-8 -*-
from base.base import Base
from page import *


class HealthyPage(Base):
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    def healthy_page(self):
        # 点击健康态势入口
        self.click_5(healthy_entrance)
        # 健康态势断言
        self.assert_png("健康态势页面", healthy_assert)


if __name__ == '__main__':
    HealthyPage().healthy_page()
