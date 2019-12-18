# -*- coding: utf-8 -*-

import unittest
from BeautifulReport import BeautifulReport
from test_cases.market.test_market import TestCheckMarket
from airtest.core.android.adb import *
from airtest.core.api import connect_device, start_app
from lib.utils import Data


def run_case():
    """
    执行代码前获取 device，并取第一个 device 进行测试
    如果没有获取到 device，不做任何操作
    """

    adb = ADB()
    device_list = adb.devices()
    print(device_list)
    if len(device_list) >= 1:
        androd_device = 'Android://127.0.0.1:5037/' + device_list[0][0]
        connect_device(androd_device)
        package_name = Data.android_package
        start_app(package_name)

        test_suite = suite()
        result = BeautifulReport(test_suite)
        test_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        report_name = '测试报告'
        result.report(filename=report_name, description=report_name + test_date, report_dir='./report',
                      log_path='report',
                      theme='theme_default')
    else:
        print('！！！ 没有连接设备')


def suite():
    """
    return test suite
    """

    test_suite = unittest.TestSuite()
    test_suite.addTests([TestCheckMarket('test_check_market')])
    return test_suite


if __name__ == '__main__':
    run_case()
