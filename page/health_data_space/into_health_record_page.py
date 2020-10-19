# -*- coding: utf-8 -*-
import time
from base.base import Base
from page import *


class IntoHealthRecordPage(Base):
    # 公共变量----元素
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    """健康档案页面"""

    def into_health_record_page(self):
        self.click_3(blgy_zk_click)
        self.assert_png("基本信息正确", blgy_zk_duanyan)
        self.click_3(blgy_guanbi)
        self.assert_png("图片和视频显示正常", tp_duanyan)
        self.click_5(jcbg_dianji)
        self.click_5(jp_png_rukou)
        for i in range(5):
            self.left()
        self.back_btn()
        # 展开
        self.click_5(zhangkai_btn)
        # 上滑两次
        for i in range(2):
            self.up()
        self.assert_png("胶片预览存在", jp_duanyan)
        self.click_5(jp_duanyan)
        self.assert_png("进入胶片成功", jr_jp_duanyan)
        # 胶片--缺少播放其他功能
        # 调用返回
        self.back_btn()
        # 向左滑动
        for i in range(2):
            self.left()
        """健康档案----一般护理页面"""
        self.click_5(ybhlj_dianji)
        # 展开
        self.click_5(zhangkai_btn)
        self.assert_png("一般护理页面展示成功", ybhlj_duanyan)
        """健康档案----转院记录页面"""
        # 滑动三次
        for i in range(3):
            self.left()
        self.click_5(zkjl_click)
        self.click_3(zkjl_zk)
        self.assert_png("转院记录页面展开成功", zkjl_duanyan)
        # 退出H5下个执行下个测试用例


if __name__ == '__main__':
    pass
