# 对象库层-基类，把定位元素的方法定义在基类中
import logging

import pytesseract
from PIL import Image
from airtest.core.api import *
from app_util import AppDriver, logger_config

# 综合基类
from conftest import BASE_DIR


class Base:
    # 对于基类而言，后续可能添加其它需要封装方法，那么这些方法也可能用到驱动对象
    def __init__(self):
        self.driver = AppDriver().start()
        logger_config()

    # 点击事件
    def p_click(self, location):
        self.driver(location).click()

    # poco----点击输入事件
    def p_click_input(self, location, txt):
        self.driver(location).click()
        text(txt, enter=False)

    # 断言
    # 图片断言
    # 断言存在
    def assert_png(self, txt, filename=""):
        try:
            assert_exists(Template(filename=filename))
            print("{}-断言成功,目标存在".format(txt))
            return "断言成功,目标存在"
        except:
            self.get_png(txt)
            logging.error("{}-断言失败,目标不存在！！！！!!".format(txt))
            return "{}-断言失败,目标不存在".format(txt)

    # 断言不存在
    def assert_not_png(self, txt, filename=""):
        try:
            assert_not_exists(Template(filename=filename))
            print("{}-断言成功,目标不存在".format(txt))
        except:
            self.get_png(txt)
            logging.error("{}-断言不成功,目标存在！！！！!!".format(txt))
            return "{}-断言失败,目标存在".format(txt)
        # 后期补判断

    # 文字断言
    def assert_txt(self, png):
        # 只能读取数字-------因为没中文包
        image = Image.open(png)
        txt = pytesseract.image_to_string(image)
        print("---------------------------")
        print(txt)
        return txt

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
        # swipe([x * 0.8, y * 0.5], [x * 0.2, y * 0.5])
        # 健康档案左滑动
        swipe([x * 0.9, y * 0.18], [x * 0.03, y * 0.18])

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
        text(txt, enter=False)

    def input(self, txt):
        text(txt, enter=False)

    # 右边沿点击和输入
    def click_6(self, filename=""):
        touch(Template(filename=filename, target_pos=6))

    def click_6_input(self, txt, filename=""):
        touch(Template(filename=filename, target_pos=6))
        text(txt, enter=False)

    # 底部中间点击
    def click_8(self, filename=""):
        touch(Template(filename=filename, target_pos=8))

    def click_9(self, filename=""):
        touch(Template(filename=filename, target_pos=9))

    def click_3(self, filename=""):
        touch(Template(filename=filename, target_pos=3))

    def click_4(self, filename=""):
        touch(Template(filename=filename, target_pos=4))

    # 底部中间点击输入
    def click_8_input(self, txt, filename=""):
        touch(Template(filename=filename, target_pos=8))
        text(txt, enter=False)

    # 清除文本
    def clear_txt(self, location):
        for i in range(location):
            keyevent("KEYCODE_DEL")

    # 返回按钮
    def back_btn(self):
        keyevent("KEYCODE_BACK")

    def get_png(self, txt):
        # msg描述测试点
        png_name = BASE_DIR + "/screenshot/{}_{}.png".format(txt, time.strftime("%Y-%m-%d-%H-%M-%S"))
        snapshot(filename=png_name, msg=txt)
        return snapshot(filename=png_name, msg=txt)

    # 删除图片和日记
    pass
