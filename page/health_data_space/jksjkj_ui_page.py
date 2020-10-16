# -*- coding: utf-8 -*-
import time
from base.base import Base
from page import *


class JUIPage(Base):
    # 公共变量----元素
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    def personal_center_page(self):
        # ----------------------------------------------------
        """个人中心页面"""
        # 搜索框按钮
        self.p_click(search_btn)
        # 输入要搜索的内容
        self.p_click_input(search_box, "粤信云")
        # 点击目标
        self.p_click(target)
        self.click_5(jksjkj_rukou)
        print("个人中心页面")
        self.assert_png("个人中心页面进入成功", grzx_duanyan)

        # ------------------------------------------------------
        """健康档案----健康态势页面"""
        self.click_5(jkts_rukou)
        self.click_5(jkda_rukou)
        # test_03-----档案判断————————————
        self.assert_png("病例概要进入成功", jr_jkda_duanyuan)
        self.click_3(blgy_zk_click)
        self.assert_png("基本信息正确", blgy_zk_duanyan)
        self.click_3(blgy_guanbi)
        self.assert_png("图片和视频显示正常", tp_duanyan)
        self.click_5(jcbg_dianji)
        # # ----------需要修改
        # self.up()
        # self.up()
        # self.up()
        # self.assert_png("胶片预览存在", jp_duanyan)
        # self.click_5(jp_duanyan)
        # self.assert_png("进入胶片成功", jr_jp_duanyan)
        # # 调用返回
        # self.back_btn()
        # 滑动两次

        """健康档案----一般护理页面"""
        time.sleep(1)
        self.left()
        self.left()
        self.click_5(ybhlj_dianji)
        #
        self.click_3(ybhlj_zk)

        self.assert_png("页面展示成功", ybhlj_duanyan)

        """健康档案----转院记录页面"""
        # 滑动三次
        self.left()
        self.left()
        self.left()
        self.click_5(zkjl_click)
        self.click_3(zkjl_zk)
        self.assert_png("页面展开成功", zkjl_duanyan)

        # ------------------------------------------------------
        """退出H5"""
        # 调用微信退出H5页面
        self.p_click(quit_h5_btn)
        # 调用上面的健康数据空间入口
        self.click_5(jksjkj_rukou)
        self.click_5(dtm_click)
        # 调用上滑
        # time.sleep(1)
        # self.up()
        # # 点击分享按钮
        # self.click_5(fxsq_click)
        self.p_click("android.support.v7.widget.LinearLayoutCompat")
        self.click_5(fsgpy_click)
        self.click_5(syc_photo_click)
        # 调用搜索的代码
        self.input("查看后分享四叶草的健康档案给我")
        self.click_5(fs_click)
        self.p_click(quit_h5_btn)
        # 调用退出H5
        time.sleep(3)
        self.back_btn()
        time.sleep(1)
        self.back_btn()
        # 返回*2

        # ------------------------------------------------------
        """健康档案处理"""
        self.click_5(syc_photo_click)
        # 等待1分钟
        time.sleep(1)
        self.click_5(sqxxlj_click)

        time.sleep(3)
        self.click_5(syc_photo_click)
        self.click_5(datb_click)
        # self.assert_png("进入患者健康档案成功", hzda_duanyan)
        self.click_5(wztb_click)
        self.click_5(kjcd_click)
        self.up()
        self.click_5(qd_click)
        # self.assert_png(jcdfs)
        self.p_click(quit_h5_btn)
        self.back_btn()
        # 调用微信退出H5
        # 点击输入框，发送自动化脚本运行完成
        # 点击发送
        # 调用返回


if __name__ == '__main__':
    JUIPage().jksjkj_ui_page()
