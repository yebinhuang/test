# -*- coding: utf-8 -*-
import time
from base.base import Base
from page import *


class HealthRecordPage(Base):
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    """健康档案页面"""

    def health_record_page(self):
        # 断言
        self.click_5(health_record_entrance)
        self.assert_png("病例概要进入成功", cases_of_the_profile_assert)


if __name__ == '__main__':
    HealthRecordPage().health_record_page()
