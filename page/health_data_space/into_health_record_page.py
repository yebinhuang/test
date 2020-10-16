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
        self.assert_png("病例概要进入成功", jr_jkda_duanyuan)
        self.click_3(blgy_zk_click)
        self.assert_png("基本信息正确", blgy_zk_duanyan)
        self.click_3(blgy_guanbi)
        self.assert_png("图片和视频显示正常", tp_duanyan)
        self.click_5(jcbg_dianji)


if __name__ == '__main__':
    HealthRecordPage().health_record_page()
