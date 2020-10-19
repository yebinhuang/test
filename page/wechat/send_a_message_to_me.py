# 发送信息给四叶草
# -*- coding: utf-8 -*-
import logging
import time
from base.base import Base


class SendAMessageToMe(Base):
    # 公共变量----元素
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    """健康档案页面"""

    def send_a_message_to_me(self, txt1, txt2):
        # 搜索框按钮
        self.p_click("com.tencent.mm:id/f8y")
        # 输入要搜索的内容
        self.p_click_input("com.tencent.mm:id/bhn", txt1)
        print('向【{}】{}发送信息'.format(txt1, "用户"))
        # 点击目标
        self.p_click("com.tencent.mm:id/gbv")
        input_txt = txt2 + "-时间：{}".format(time.strftime("%Y-%m-%d-%H:%M-%S"))
        self.p_click_input("com.tencent.mm:id/g78", input_txt)
        time.sleep(2)
        try:
            self.p_click("com.tencent.mm:id/anv")
        except:
            logging.error('向【{}】{}发送信息-失败！！！！！！'.format(txt1, "用户"))


if __name__ == '__main__':
    SendAMessageToMe().send_a_message_to_me("四叶草", "TEST")
