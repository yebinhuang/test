# 第一次进入数据空间
from base.base import Base
from page import *


class ForTheFirstTimePage(Base):
    # 公共变量----元素
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    # 统一用2次返回，退回微信主页的判断
    def for_the_first_time_page(self):
        self.assert_png("首次进入健康数据空间", xinxishouquan)
        self.click_8(xinxishouquan)


if __name__ == '__main__':
    ForTheFirstTimePage().for_the_first_time_page()
