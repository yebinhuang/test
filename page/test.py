# 微信输入框输入并发送信息
# -*- coding: utf-8 -*-
import time
from base.base import Base


# # 表情信息
# txt = "[微笑][撇嘴][色][发呆][得意][流泪][害羞][闭嘴][睡][大哭][尴尬][发怒]" \
#       "[调皮][呲牙][惊讶][难过][囧][抓狂][吐][偷笑][愉快][白眼][傲慢][困]" \
#       "[惊恐][流汗][憨笑][悠闲][奋斗][咒骂][疑问][嘘][晕][衰][骷髅][敲打]" \
#       "[再见][擦汗][抠鼻][鼓掌][坏笑][左哼哼][右哼哼][哈欠][鄙视][委屈][快哭了]" \
#       "[阴险][亲亲][可怜][菜刀][西瓜][啤酒][咖啡][猪头][玫瑰][凋谢][嘴唇][爱心]" \
#       "[心碎][蛋糕][炸弹][便便][月亮][太阳][拥抱][强][弱][握手][胜利][抱拳][勾引]" \
#       "[拳头][OK][跳跳][发抖][怄火][转圈][嘿哈][捂脸][奸笑][机智][皱眉][耶][吃瓜]" \
#       "[加油][汗][天啊][Emm][社会社会][旺柴][好的][打脸][加油加油][哇][红包][發][福]"
# 表情包信息发送
class TestPage(Base):
    # 公共变量----元素
    def __init__(self):
        # 重写父类初始化方法
        super().__init__()

    """健康档案页面"""

    def test_page(self):
        for i in range(100):
            txt = "{}".format(time.strftime("%Y-%m-%d-%H-%M-%S"))
            self.p_click_input("com.tencent.mm:id/g78", txt)
            time.sleep(2)
            self.p_click("com.tencent.mm:id/anv")


TestPage().test_page()
