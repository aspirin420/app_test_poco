# -*- coding=utf-8 -*-

import os, sys
from lib.base_app import BaseAppCase

abs_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(abs_dir)


class TestSearch(BaseAppCase):

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

    def test_search(self):
        """
        验证搜索功能，判断搜索规则是否在搜索结果内
        """

        self.poco('**.android.debug:id/app_coor_layout').wait_for_appearance() # 等待元素出现
        self.poco('**.android.debug:id/title_bar_right').click() # 点击事件
        self.poco(text='请输入').set_text('001') # 输入框输入内容
        result_obj_list = self.poco(name='**.android.debug:id/market_tv_stock_item_name') # 获取搜索结果列表内容
        result_list = [stock.get_text() for stock in result_obj_list]
        self.save_img('模糊搜索')
        search_list = ['长和', '平安银行', '上证指数', '沪港联合'] # 规则内的数据不在搜索结果内，说明失败
        result = True
        for i in search_list:
            if i in result_list:
                continue
            else:
                result = result and False
                break
        self.poco('**.android.debug:id/market_tv_stock_search_cancel').wait_for_appearance()
        self.poco('**.android.debug:id/market_tv_stock_search_cancel').click() # 返回到 app 首页
        self.assertEqual(result, True) # 判断 case 结果
