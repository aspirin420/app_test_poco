# -*- coding=utf-8 -*-

import os, sys
from lib.base_app import BaseAppCase

abs_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(abs_dir)


class TestCheckMarket(BaseAppCase):

    def setUp(self):
        """
        当前 case 的前置条件：执行 case 前的准备工作
        """

        pass

    def tearDown(self):
        """
        当前 case 的后置条件：执行 case 后的收尾工作
        """

        pass

    def test_check_market(self):
        """
        查看资产页面是否加载出来
        """

        self.poco(text="登录/注册").click()
        self.poco("**.android.debug:id/et_phone").set_text('13**********')
        self.poco(text="下一步").click()

        self.poco(text='验证码已发送成功!').wait(2)
        result = self.poco('**.android.debug:id/tv_summary_title').get_text()
        self.save_img('test_check_asset') # 截图并保存
        self.assertEqual(result, '总资产(USD)')
