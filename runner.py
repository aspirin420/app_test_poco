# -*- coding: utf-8 -*-

import unittest
from BeautifulReport import BeautifulReport
from test_cases.market.test_market import TestCheckMarket
from airtest.core.android.adb import *
from lib.utils import connect_android, connect_iOS


def run_case():
    """
    做 iOS 还是 Android 测试可以根据 ./lib/utils 里面的方法进行判断
    此处直接手动改代码处理，没有自动化，因为 iOS 自动化选择 device 比较麻烦
    对于Android：
        执行代码前获取 device，并取第一个 device 进行测试
        如果没有获取到 device，打印日志
    """

    is_connect_iOS = connect_iOS()
    is_connect_android = connect_android()
    if is_connect_android or is_connect_iOS:
        test_suite = suite()
        result = BeautifulReport(test_suite)
        test_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        report_name = '测试报告'
        result.report(filename=report_name, description=report_name + test_date, report_dir='./report',
                      log_path='report',
                      theme='theme_default')
    else:
        print('!!! 没有连接设备')


def suite():
    """
    return test suite
    """

    test_suite = unittest.TestSuite()
    test_suite.addTests([TestCheckMarket('test_check_market')])
    return test_suite


if __name__ == '__main__':
    run_case()
