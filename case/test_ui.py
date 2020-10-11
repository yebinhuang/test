from page.chat_page import TencentPage
from page.tencent_find_page import TencentFindPage


class Test_o:
    def test_01(self):
        TencentPage().clear_chat_logs_page("粤信云")
        TencentFindPage().tencent_find_page("粤信云")
