# 图片地址
site = "G:/app_airtest_auto/png/"

# --------------------------------------   A.微信app--wechat_png/   --------------------------------------------
# 取消关注公众号与关注公众号

# 清除缓存

# 主页
wechat_png = "wechat_png/"
A = site + wechat_png
zhuye = A + "zhuye.png"
# # 退出H5页面按钮
quit_h5_btn = "com.tencent.mm:id/dn"
# # 微信返回键按钮
# poco("com.tencent.mm:id/rs").click()
# 搜索框按钮
search_btn = "com.tencent.mm:id/f8y"
# 搜索要搜索的内容
search_box = "com.tencent.mm:id/bhn"
# 点击目标
target = "com.tencent.mm:id/gbv"
# 删除聊天记录
yue_xin_yun = A + "yuexinyun.png"
jksjkj = A + "jksjkj.png"
clear_chat_btn1 = A + "clear_chat_btn1.png"
clear_chat_btn2 = A + "clear_chat_btn2.png"

# 图片
photo_btn1 = A + "photo_btn.png"
photo_btn2 = A + "photo_btn2.png"
photo = A + "photo.png"

# --------------------------------------   B.医生工作站--doctor_png/   --------------------------------------------
# 公用元素
doctor = "doctor_png/"
B = site + doctor
# 下一步
next_btn = B + "next_btn.png"
# 确认按钮
affirm_btn = B + "affirm_btn.png"
# 完成按钮
wancheng_btn = B + "wancheng_btn.png"

# 医生工作站
"""1.医生认证"""
# 医生认证入口
doctor_attestation_entrance = B + "doctor_attestation_entrance.png"
# 医生姓名
doctor_name_box = B + "doctor_name_box.png"
# 医生号码
doctor_num_box = B + "doctor_num_box.png"
# 医生身份证
doctor_idcard_box = B + "doctor_idcard.png"
# 发送验证码
doctor_attestation_code = B + "doctor_attestation_code.png"
# 验证码输入框
doctor_code_box = B + "doctor_code_box.png"
# 就职医院
doctor_attestation_hospital = B + "doctor_attestation_hospital.png"
# 医院
click_hospital = B + "click_hospital.png"
# 点击认证按钮
click_attestation_btn = B + "click_attestation_btn.png"
# 完善信息
click_attestation_btn2 = B + "click_attestation_btn2.png"
# 填写信息
# 缺少身份证
pass
# 选择科室
keshi_btn = B + "keshi_btn.png"
# 确认----用公共元素
# 选择职称
zhicheng_btn = B + "zhicheng_btn.png"
# 上传工作证
gzz_push_btn1 = B + "gzz_push_btn1.png"
gzz_push_btn2 = B + "gzz_push_btn2.png"
# 调用公共元素,缺少拖动动作
pass
# 上传执业证
zhiyezheng_btn = B + "zhiyezheng_btn.png"
zhiyezheng_btn2 = B + "zhiyezheng_btn2.png"
# 上传资格证
zigezheng_btn1 = B + "zigezheng_btn1.png"
zigezheng_btn2 = B + "zigezheng_btn2.png"
# 个人简介
gerenjianjie_btn = B + "gerenjianjie_btn.png"
# 擅长领域
shanchanglingyu_btn = B + "shanchanglingyu_btn.png"
# 缺少后面的
# 提交按钮
tijiao_btn = B + "tijiao_btn.png"
# 返回数据空间
fanhui_jksjkj_btn = B + "fanhui_jksjkj_btn.png"

# --------------------------------------   C.健康数据空间--health_data_space_png/   --------------------------------------
# 清除token


# 项目元素地址
health_data_space_png = "health_data_space_png/"
C = site + health_data_space_png
# 首次进入健康数据空间---信息授权页面(利用click_8的方法进行点击)
authorization_information = C + "authorization_information.png"
# 健康数据空间入口(微信公众号跳转H5页面)
health_data_space_entrance = C + "health_data_space_entrance.png"

"""个人中心页面"""
# 进入个人中心断言的元素
personal_center_assert = C + "personal_center_assert.png"
# 备注：用户认证----选择下方的图标元素做为入口
# 健康态势入口(调用时，需要调用上滑self.up())
healthy_entrance = C + "healthy_entrance.png"
# 动态码入口
dynamic_code_entrance = C + "dynamic_code_entrance.png"
# 健康日记入口
health_diary_entrance = C + "health_diary_entrance.png"
# 我的名片入口
my_name_card_entrance = C + "my_name_card_entrance.png"

"""健康态势页面(健康档案页面)"""
# 健康态势断言
healthy_assert = C + "healthy_assert.png"
# 健康档案入口
health_record_entrance = C + "health_record_entrance.png"

pass
cases_of_the_profile_assert = C + "cases_of_the_profile_assert.png"

blgy_zk_click = C + "blgy_zk_dianji.png"

blgy_zk_duanyan = C + "blgy_zk_duanyan.png"

blgy_guanbi = C + "blgy_guanbi.png"

tp_duanyan = C + "tp_duanyan.png"
# 健康报告点击
jcbg_dianji = C + "jcbg_dianji.png"
# 胶片图片入口
jp_png_rukou = C + "jp_png_rukou.png"
# 展开按钮------仅一个按钮时可用
zhangkai_btn = C + "zhangkai_btn.png"
# 关闭展开按钮
close_zhangkai_btn = C + "close_zhangkai_btn.png"
# 播放胶片
# 停止播放与翻页

# 胶片断言
jp_duanyan = C + "jp_duanyan.png"

jr_jp_duanyan = C + "jr_jp_duanyan.png"

ybhlj_dianji = C + "ybhlj_dianji.png"

ybhlj_zk = C + "ybhlj_zk.png"

ybhlj_duanyan = C + "ybhlj_duanyan.png"

zkjl_click = C + "zkjl_click.png"

zkjl_zk = C + "zkjl_zk.png"

zkjl_duanyan = C + "zkjl_duanyan.png"

dtm_click = C + "dtm_click.png"

fxsq_click = C + "fxsq_click.png"

fsgpy_click = C + "fsgpy_click.png"

fs_click = C + "fs_click.png"

syc_photo_click = C + "syc_photo_click.png"

sqxxlj_click = C + "sqxxlj_click.png"

hzda_duanyan = C + "hzda_duanyan.png"

wztb_click = C + "wztb_click.png"

kjcd_click = C + "kjcd_click.png"

qd_click = C + "qd_click.png"

jcdfs = C + "jcdfs.png"

datb_click = C + "datb_click.png"
