# -*- coding: utf-8 -*-
import time
from base.base import Base
from page import *
import logging


class PersonalCenterPage(Base):
    # 公共变量----元素
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    def personal_center_page(self, txt):
        """个人中心页面"""
        # 搜索框按钮
        self.p_click(search_btn)
        # 输入要搜索的内容
        self.p_click_input(search_box, txt)
        logging.info('------------------{}{}-----------------------'.format(txt, "公众号"))
        # 点击目标
        self.p_click(target)
        self.click_5(jksjkj_rukou)
        self.assert_png("个人中心页面", grzx_duanyan)


if __name__ == '__main__':
    PersonalCenterPage().personal_center_page("粤信云")
