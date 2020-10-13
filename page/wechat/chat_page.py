# -*- coding: utf-8 -*-
# UI界面测试
from base.base import Base
from page import *


class TencentPage(Base):
    # 公共变量----元素
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    # 清除聊天记录
    """png：判断的图片"""

    def clear_chat_logs_page(self, png):
        # 判断是否存在目标
        b = "断言成功,目标存在"
        d = self.assert_not_png("判断是否存在", png)
        if b in d:
            print("存在")
            self.long_png_press(png)
            # 选择删除
            self.click_5(clear_chat_btn1)
            self.click_5(clear_chat_btn2)
        else:
            print("聊天用户不存在，继续执行")


if __name__ == '__main__':
    pass
