"""流程"""
# 打开微信app
# 注销用户
# 移动端——认证医生
# 后台审核医生
# 退出浏览器

# 移动端
# -*- coding: utf-8 -*-
# UI界面测试
from base.base import Base
from page import *


# 微信寻找目标
class TheDoctorCertifiedPage(Base):
    # 公共变量----元素
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    # 选择搜索的内容
    """txt:搜索的内容"""

    def the_doctor_certified_page(self):
        # # 需要调用微信发送信息功能
        # self.click_5(doctor_attestation_entrance)
        # try:
        #     self.click_8_input("小叶", doctor_name_box)
        # except:
        #     print("医生已注册，无需填写姓名")
        # try:
        #     self.click_8_input("16530800941", doctor_num_box)
        # except:
        #     print("医生已注册，无需填写手机号码")
        # self.click_5(doctor_attestation_code)
        # self.click_5_input("123123", doctor_code_box)
        # self.click_8_input("医院", doctor_attestation_hospital)
        #
        # try:
        #     self.click_5(click_hospital)
        # except:
        #     print("医院不存在")
        # self.up()
        # # 点击“认证”
        # self.click_5(click_attestation_btn)
        # # 完善信息
        # self.click_9(click_attestation_btn2)
        # 填写信息
        try:
            self.click_5_input("440982200104294294", doctor_idcard_box)
        except:
            print("找不到，医生身份证")
        self.click_5(next_btn)
        # 上传医生
        self.click_5(keshi_btn)
        self.click_6(affirm_btn)
        self.click_5(zhicheng_btn)
        self.click_6(affirm_btn)
        self.click_6(gzz_push_btn1)
        self.click_5(gzz_push_btn2)
        # 照片上传公共元素
        self.click_5(photo_btn1)
        self.click_8(photo_btn2)
        self.click_5(photo)
        # 完成
        self.click_6(wancheng_btn)
        self.up()
        self.click_5(zhiyezheng_btn)
        self.click_5(zhiyezheng_btn2)
        # 照片上传公共元素
        self.click_5(photo_btn1)
        self.click_8(photo_btn2)
        self.click_5(photo)
        # 完成
        self.click_6(wancheng_btn)
        self.click_6(zigezheng_btn1)
        self.click_6(zigezheng_btn2)
        # 照片上传公共元素
        self.click_5(photo_btn1)
        self.click_8(photo_btn2)
        self.click_5(photo)
        # 完成
        self.click_6(wancheng_btn)
        self.up()
        self.click_5(next_btn)
        self.click_5_input("治病", gerenjianjie_btn)
        self.click_5_input("治病", shanchanglingyu_btn)
        # 缺少确认按钮和返回数据空间
        self.up()
        self.click_5(tijiao_btn)
        self.click_5(fanhui_jksjkj_btn)

        """调用后台认证"""
        # CertifiedDoctor().certified_by_a_doctor()


if __name__ == '__main__':
    TheDoctorCertifiedPage().the_doctor_certified_page()
