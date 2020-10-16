# -*- coding: utf-8 -*-
import time
from base.base import Base
from page import *
from BeautifulReport import BeautifulReport


class HealthRecordPage(Base):
    # 公共变量----元素
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    """健康档案页面"""
    def health_record_page(self):
        self.click_5(jkts_rukou)
        self.click_5(jkda_rukou)
        # 断言
        self.assert_png("健康档案页面")


if __name__ == '__main__':
    HealthRecordPage().health_record_page()