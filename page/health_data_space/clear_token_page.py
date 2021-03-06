# 清除token
from base.base import Base
from page import *


class ClearTokenPage(Base):
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    # 统一用2次返回，退回微信主页的判断
    def clear_token_page(self):
        self.assert_png("首次进入健康数据空间", authorization_information)
        self.click_8(authorization_information)


if __name__ == '__main__':
    ClearTokenPage().clear_token_page()