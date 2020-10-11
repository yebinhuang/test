# -*- coding: utf-8 -*-
# UI界面测试
from base.base import Base
from page import *


# 微信寻找目标
class TencentFindPage(Base):
    # 公共变量----元素
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    # 选择搜索的内容
    """txt:搜索的内容"""

    def tencent_find_page(self, txt):
        # 搜索框按钮
        self.p_click(search_btn)
        # 输入要搜索的内容
        self.p_click_input(search_box, txt)
        # 点击目标
        self.p_click(target)


if __name__ == '__main__':
    pass
