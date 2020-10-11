# 对象库层-基类，把定位元素的方法定义在基类中
from airtest.core.api import *

from app_util import AppDriver


# 综合基类


class Base:
    # 对于基类而言，后续可能添加其它需要封装方法，那么这些方法也可能用到驱动对象
    def __init__(self):
        self.driver = AppDriver().start()

    # 点击事件
    def p_click(self, location):
        self.driver(location).click()

    # poco----点击输入事件
    def p_click_input(self, location, txt):
        self.driver(location).click()
        text(txt)

    # 断言
    # 图片断言
    # 断言存在

    def assert_png(self, txt, filename=""):
        try:
            assert_exists(Template(filename=filename), txt)
            print("断言成功,目标存在")
            return "断言成功,目标存在"
        except:
            print("断言失败,目标不存在")
            return "断言失败,目标不存在"

    # 断言不存在
    def assert_not_png(self, txt, filename=""):
        try:
            assert_not_exists(Template(filename=filename), txt)
            print("断言成功,目标不存在")
            return "断言成功,目标不存在"
        except:
            print("断言成功,目标存在")
            return "断言成功,目标存在"
        # 后期补判断

    # 文字断言
    def assert_txt(self, txt, filename=""):
        pass

    # 等待---参考----https://blog.csdn.net/qq_42775047/article/details/106444316
    """显示等来"""

    def wait(self):
        pass

    # 原生桌面长按
    def long_press(self, txt):
        pass

    # 图片长按
    def long_png_press(self, filename=""):
        touch(Template(filename=filename), duration=1)

    # 微信删除聊天记录
    # # 长按
    # self.long_png_press(yue_xin_yun)
    # # 选择删除
    # self.click_5(clear_chat_btn1)
    # self.click_5(clear_chat_btn2)
    # 获取屏幕大小的方法
    def slide(self):
        print("获取屏幕大小：", self.driver.get_screen_size())

    # 滑动屏幕操作
    def up(self):
        xy = self.driver.get_screen_size()
        x = xy[0]
        y = xy[1]
        swipe([x * 0.5, y * 0.8], [x * 0.5, y * 0.2])

    def down(self):
        xy = self.driver.get_screen_size()
        x = xy[0]
        y = xy[1]
        swipe([x * 0.5, y * 0.2], [x * 0.5, y * 0.8])

    def left(self):
        xy = self.driver.get_screen_size()
        x = xy[0]
        y = xy[1]
        swipe([x * 0.8, y * 0.5], [x * 0.2, y * 5])

    def right(self):
        xy = self.driver.get_screen_size()
        x = xy[0]
        y = xy[1]
        swipe([x * 0.2, y * 0.5], [x * 0.8, y * 0.5])

    """filename---图片"""
    """threshold---识别度"""
    """target_pos---位置---默认为中心点击，6位右边，8位底部中心以此类推"""
    """rgb---黑白处理后识别----默认为False,开的话为True"""

    # 中心点击
    def click_5(self, filename=""):
        touch(Template(filename=filename))

    # 中心点击和输入
    def click_5_input(self, txt, filename=""):
        touch(Template(filename=filename))
        text(txt)

    # 右边沿点击和输入
    def click_6(self, txt, filename=""):
        touch(Template(filename=filename, target_pos=6))
        text(txt)

    # 底部中间点击
    def click_8(self, filename=""):
        touch(Template(filename=filename, target_pos=8))

    # 底部中间点击输入
    def click_8_input(self, txt, filename=""):
        touch(Template(filename=filename, target_pos=8))
        text(txt)

    # 清除文本
    def clear_txt(self, location):
        for i in range(location):
            keyevent("KEYCODE_DEL")
